from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = b'dev'

    from .routes import bp

    app.register_blueprint(bp)

    return app
