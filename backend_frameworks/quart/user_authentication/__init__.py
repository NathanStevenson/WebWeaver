import quart
from quart import redirect, url_for
from quart_schema import validate_request
from quart_auth import login_required, login_user, logout_user, Unauthorized, AuthUser

from ..db_interface.user_model import User
from ..db_interface import db_interface
from . import schemas
from . import auth_utils

bp = quart.Blueprint('authentication', __name__, url_prefix="/")

# private route which serves /private HTML template; default tab shown on the web - only accessed with successful login
@login_required
async def private_route():
    return await quart.render_template('private.html')

# if you fail a login requirement instead of default 401 unauthorized serve this custom 
@bp.errorhandler(Unauthorized)
async def custom_unauthorized_page():
    return await quart.render_template('unauthorized.html')

# serve the sign_up form - also present the option here to Login with Google/Apple/GitHub? - custom login
@bp.get("sign_up")
async def sign_up_form():
    return await quart.render_template('sign_up.html')

# receives POST request when the user signs up; checks that no other user with that email exists - hashes password and adds it into DB
@validate_request(schemas.UserSignup)
# validates the incoming request with pydantic; data will hold the validated json request params
@bp.post("sign_up")
async def process_sign_up(data: schemas.UserSignup):
    async with db_interface.create_session() as session:
        email_exists = User.get_user_by_email(session, data.email)
        if email_exists is not None:
            return {"error_msg": f"Email already exists for {data.email}. Try logging in or signing up with another email"}
        else:
            # salt + hash the incoming password via bcrypt; create a new user; add it to SQLAlchemy session; put it in DB
            hashed_password = auth_utils.hash_password(data.password)
            new_user = User(email=data.email, hashed_password=hashed_password)
            User.add(session, new_user)
            # redirect user to the private route which reflects their email back to them if just basic auth is wanted; in future have 2FA to verify their email is right before adding user to the DB of our site
            return redirect(url_for('authentication.private'))


# serve the login form
@bp.get("login")
async def login_form():
    return await quart.render_template('login.html')

# receives POST request when the user signs up; checks that no other user with that email exists - hashes password and adds it into DB
@validate_request(schemas.UserSignup)
# validates the incoming request with pydantic; data will hold the validated json request params
@bp.post("login")
async def process_login(data: schemas.UserSignup):
    async with db_interface.create_session() as session:
        # check if the user exists
        user = User.get_user_by_email(session, data.email)
        # verify that the password matches the hashed password
        if user and auth_utils.verify_password(data.password, user.hashed_password):
            login_user(AuthUser(str(user.id)))  # quart uses string as AuthUser - access ID via current_user.auth_id, current_user.is_authenticated bool for logged in or out user
            return redirect(url_for('authentication.private'))
        else:
            return {"error_msg": "Unsuccessful login!"}
        
@bp.get("logout")
async def process_logout():
    logout_user()
    return redirect(url_for('html_routes.index'))