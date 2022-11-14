from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()

# app factory copied from mega-tutorial
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    from .base import routes
    app.register_blueprint(routes.base)

    from .auth import routes
    app.register_blueprint(routes.users)

    from .posts import routes
    app.register_blueprint(routes.post)

    return app


# this last line needs to be added for migrate to create table
from application import models
