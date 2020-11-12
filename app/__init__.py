from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()
login.login_message = "Você deve fazer login para acessar esta página!"
login.login_view = "auth.login"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    bootstrap.init_app(app)
    login.init_app(app)

    from app.website import website as website_blueprint
    app.register_blueprint(website_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from app import views, models

    return app
