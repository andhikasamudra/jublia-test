from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    mail.init_app(app)

    from app.routes.email import email_bp

    app.register_blueprint(email_bp)

    return app, db
