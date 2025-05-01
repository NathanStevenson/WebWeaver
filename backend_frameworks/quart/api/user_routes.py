import quart
from quart import request

from ..db_interface.user_model import User
from ..db_interface import db_interface

bp = quart.Blueprint('users', __name__, url_prefix="/users")

# replace with pydantic schema validation
@bp.post("")
async def create_user():
    data = await request.get_json()
    user_name = data.get("user_name")
    email = data.get("email")

    if not user_name or not email:
        return {"error": "user_name and email required"}, 400

    user = User(user_name=user_name.strip(), email=email.lower())  # Transform input
    async with db_interface.create_session() as session:
        try:
            user = await User.add(session, user)
            return user.to_dict()
        except Exception as e:
            return {"error": str(e)}, 500


@bp.put("<int:user_id>")
async def update_user(user_id):
    data = await request.get_json()
    async with db_interface.create_session() as session:
        user = await User.get_by_id(session, user_id)
        if not user:
            return {"error": "User not found"}, 404

        # Update fields with validation/transformation
        if "user_name" in data:
            user.user_name = data["user_name"].strip()
        if "email" in data:
            user.email = data["email"].lower()

        try:
            user = await User.edit(session, user)
            return user.to_dict()
        except Exception as e:
            return {"error": str(e)}, 500


@bp.delete("<int:user_id>")
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
        

@bp.get("<int:user_id>")
async def get_user(user_id):
    async with db_interface.create_session() as session:
        user = await User.get_by_id(session, user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict()


@bp.get("")
async def get_users():
    async with db_interface.create_session() as session:
        all_users = await User.get_all(session)
        return list(map(lambda user: user.to_dict(), all_users))