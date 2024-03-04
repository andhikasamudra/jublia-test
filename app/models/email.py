from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean


class Emails(BaseModel):
    __tablename__ = "emails"

    event_id = Column(Integer, nullable=False)
    subject = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    sent_timestamp = Column(DateTime(timezone=True), nullable=False)
    is_sent = Column(Boolean, default=False)
