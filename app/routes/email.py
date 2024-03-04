# routes/email.py
from datetime import datetime, timedelta

import jsonschema
import pytz
from flask import Blueprint, request, current_app

from app import db
from app.models.email import Emails
from app.schemas import save_email
from app.utils.constants import ErrorCode
from app.utils.responses import create_response

email_bp = Blueprint("email", __name__, url_prefix="")


@email_bp.route("/save_emails", methods=["POST"])
def register():
    data = request.get_json()

    try:
        jsonschema.validate(instance=data, schema=save_email.validate_schema)
    except jsonschema.ValidationError as e:
        return create_response(error_key={"message": str(e), "code": 400})

    if not data:
        return create_response(error_key=ErrorCode.INVALID_JSON_DATA)

    try:
        parsed_date = datetime.strptime(data.get("sent_timestamp"), "%d %b %Y %H:%M")
        from_zone = pytz.timezone("Asia/Singapore")

        to_zone = pytz.utc
        local_time = from_zone.localize(parsed_date)

        utc_time = local_time.astimezone(to_zone)

        new_email = Emails(
            event_id=data.get("event_id"),
            subject=data.get("subject"),
            content=data.get("content"),
            sent_timestamp=utc_time,
        )
        db.session.add(new_email)
        db.session.commit()
        return create_response(error_key=ErrorCode.EMAIL_SAVED)
    except Exception as e:
        db.session.rollback()
        return create_response(error_key={"message": str(e), "code": 500})
