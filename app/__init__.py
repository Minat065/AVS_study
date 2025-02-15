import os

from flask import Flask
from app.views.user_views import users_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(users_bp)

  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return app