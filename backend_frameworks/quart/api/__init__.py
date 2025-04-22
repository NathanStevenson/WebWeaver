import quart

bp = quart.Blueprint('api', __name__, url_prefix="/api")

# Import all related api files
from . import user_routes

# Register all related api blueprints
bp.register_blueprint(user_routes.bp)

# All routes served under "/api"
@bp.get('/hello_world')
async def hello_world():
    return {"message": "Hello World from API!", "hint": "Quart formats dictionaries returns to proper JSON args (cool!)"}