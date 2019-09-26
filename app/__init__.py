# app\__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong' # flask will delete session and cookies, and force user to re-login after logging out
bcrypt = Bcrypt()

def create_app(config_type): # Pass dev, test, or prod config type
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')      # <current dir>\config\<config_type>.py
    app.config.from_pyfile(configuration)

    # Initialize classes that we imported
    db.init_app(app) # bind database to flask app
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # import blueprint for catalog
    from app.catalog import main        # import main blueprint from app\catalog\__init__.py
    app.register_blueprint(main)

    # import blueprint for authentication
    from app.auth import authentication
    app.register_blueprint(authentication)

    return app


