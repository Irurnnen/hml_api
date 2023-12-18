#!/usr/bin/env python3
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings.api_spec import get_apispec
from settings.configs import env
from settings.swagger import swagger_ui_blueprint, SWAGGER_URL

db = None


def create_app(config_name) -> Flask:
    flask_app = Flask(__name__)
    config_module = f"settings.configs.{config_name.capitalize()}Config"
    flask_app.config.from_object(config_module)
    db = SQLAlchemy(flask_app)

    flask_app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @flask_app.route("/swagger")
    def create_swagger_spec():
        return json.dumps(get_apispec(flask_app).to_dict())

    return flask_app


if __name__ == "__main__":
    app = create_app(env.str("APPLICATION_CONFIG", "development"))
    app.run(host="0.0.0.0", debug=env.bool("APPLICATION_DEBUG", False))
