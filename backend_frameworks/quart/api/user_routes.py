import quart
from quart import request

from quart_project.db_interface.user_model import User
from quart_project.db_interface import db_interface

bp = quart.Blueprint('users', __name__, url_prefix="/users")

# replace with pydantic schema validation
@bp.post("/users")
async def create_user():
    data = await request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return {"error": "Name and email required"}, 400

    user = User(name=name.strip(), email=email.lower())  # Transform input
    async with db_interface.create_session() as session:
        try:
            user = await User.add(session, user)
            return {"id": user.id, "name": user.name, "email": user.email}, 201
        except Exception as e:
            return {"error": str(e)}, 500


@bp.put("/users/<int:user_id>")
async def update_user(user_id):
    data = await request.get_json()
    async with db_interface.create_session() as session:
        user = await User.get_by_id(session, user_id)
        if not user:
            return {"error": "User not found"}, 404

        # Update fields with validation/transformation
        if "name" in data:
            user.name = data["name"].strip()
        if "email" in data:
            user.email = data["email"].lower()

        try:
            user = await User.edit(session, user)
            return {"message": "User updated", "id": user.id}
        except Exception as e:
            return {"error": str(e)}, 500


@bp.delete("/users/<int:user_id>")
async def delete_user(user_id):
    async with db_interface.create_session() as session:
        user = await User.get_by_id(session, user_id)
        if not user:
            return {"error": "User not found"}, 404

        try:
            await User.delete(session, user)
            return {"message": "User deleted"}
        except Exception as e:
            return {"error": str(e)}, 500
        

@bp.get("/users/<int:user_id>")
async def get_user(user_id):
    async with db_interface.create_session() as session:
        user = await User.get_by_id(session, user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {user.name, user.email}


@bp.get("/users")
async def get_users():
    async with db_interface.create_session() as session:
        return await User.get_all(session)