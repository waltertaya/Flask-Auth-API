from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

import secrets

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app

def gen_token():
    token_len = 32
    token = secrets.token_hex(token_len)
    return token
