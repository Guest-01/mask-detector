import os

from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(__name__)
    app.secret_key = b"dev"

    from .routes import bp

    app.register_blueprint(bp)

    return app
