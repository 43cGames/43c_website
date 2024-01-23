import os

from flask import Flask, Blueprint, render_template
from app.extensions import db

def setup_models(app: Flask) -> None:
    from app.models import Example

    db.init_app(app)

# def setup_blueprints(app: Flask) -> None:
#     from app.home_blueprint import home_blueprint

#     app.register_blueprint(home_blueprint)

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("app.config.DevelopmentConfig")

    setup_models(app)
    # setup_blueprints(app)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def page_not_found(e):
        return '404: Page not found', 404
    
    @app.route('/')
    def index():
        return render_template("layout.html")
    
    return app