import quart

bp = quart.Blueprint('html_templates', __name__, url_prefix="/")

# Import all related api files

# Register all related api blueprints

# All routes served under "/"
@bp.get('/hello_world')
async def index():
    return await quart.render_template('hello_world.html', name='Quart Static HTML Jinja Template')