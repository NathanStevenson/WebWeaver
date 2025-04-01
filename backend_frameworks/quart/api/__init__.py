import quart

bp = quart.Blueprint('api', __name__, url_prefix="/api")

# Import all related api files

# Register all related api blueprints

# All routes served under "/api"
@bp.get('/hello_world')
async def index():
    return {"message": "Hello World from API!", "hint": "Quart formats dictionaries returns to proper JSON args (cool!)"}