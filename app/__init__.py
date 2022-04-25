from flask import Flask
from app.api import api_bp
from app.plugins import db, migrate


def create_app(app_config=None):
    app = Flask(__name__)
    app.config.from_object(app_config)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprint(app)

    return app



def register_blueprint(app):
    app.register_blueprint(api_bp, url_preix='/api')