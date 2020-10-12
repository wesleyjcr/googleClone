from flask import Flask
from google_spa.ext import db
from google_spa.ext import site


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f"config.{config_name}")

    db.init_app(app)
    site.init_app(app)

    return app
