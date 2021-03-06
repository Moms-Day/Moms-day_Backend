from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from mongoengine import connect

from app.views import *

from config import Config


def create_app(*config_cls):
    """
    Creates Flask instance & initialize

    Returns:
        Flask instance
    """
    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    app_ = Flask(
        __name__,
        static_folder='{}/imgs'.format(Config.IMAGE_PATH)
    )

    for config in config_cls:
        app_.config.from_object(config)

    CORS().init_app(app_)
    JWTManager().init_app(app_)
    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)
    Router().init_app(app_)

    connect(**app_.config['MONGODB_SETTINGS'])

    app_.after_request(after_request)
    app_.register_error_handler(Exception, error_handler)

    return app_
