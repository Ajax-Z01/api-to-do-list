from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    from .auth import auth
    from .routes import api
    
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(api, url_prefix="/api")

    return app
