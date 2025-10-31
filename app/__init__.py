from flask import Flask

def crear_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    return app