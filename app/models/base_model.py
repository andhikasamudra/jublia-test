from sqlalchemy.sql import func
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    last_modified_at = db.Column(db.TIMESTAMP)
    deleted_at = db.Column(db.TIMESTAMP)
