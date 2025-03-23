from quart import Quart
import uvicorn
import argparse

import api
import html_routes

# returns a fully configured Quart application
def create_app(webweaver_config=None):
    app = Quart(__name__)

    # registers all of your top level routes / (HMTL routes), /api (JSON API routes)
    app.register_blueprint(api.bp)
    app.register_blueprint(html_routes.bp)

    # this config file is used by WebWeaver to ensure your web app does exactly what you specified
    if webweaver_config:
        app.config.update(webweaver_config)
    
    # Before serving the webserver: initialize the database connection; if the project has one
    # @app.before_serving
    # async def before_serving():
    #     await setup_database()
    
    return app

# Creates the Quart application (must be outside __main__ so uvicorn can use reload)
app = create_app()

# when running python app.py can optionally specify host / port to run the webserver on a specific ip:port
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host IP")
    parser.add_argument("--port", type=int, default=8000, help="Port number")
    args = parser.parse_args()
    
    # creates your Quart app and runs it with ASGI uvicorn
    uvicorn.run("app:app", host=args.host, port=args.port, reload=True)