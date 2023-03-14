from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    #initialise flask app
    app = Flask(__name__)

    #add configuration from object
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    from command.db import db_cmd
    app.register_blueprint(db_cmd)

    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app