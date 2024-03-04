import pytz

from app import create_app

app, _ = create_app()
app.app_context().push()

from celery import Celery
from celery.utils.log import get_task_logger
from datetime import datetime, timedelta
from app.models.email import Emails
from app.utils.email import send_email
from app import db
from sqlalchemy import and_

logger = get_task_logger(__name__)

celery = Celery("tasks")
celery.config_from_object("celery_config")


@celery.task
def send_emails():
    try:
        current_time = datetime.utcnow().replace(
            second=0, microsecond=0, tzinfo=pytz.utc
        )

        matching_emails = Emails.query.filter(
            and_(
                Emails.sent_timestamp >= current_time,
                Emails.sent_timestamp < (current_time + timedelta(minutes=1)),
                Emails.is_sent == False,
            )
        ).all()

        for email in matching_emails:
            send_email("jublia-test@testing.com", email.subject, email.content)
            email.is_sent = True
            db.session.commit()

            logger.info(f"Email sent with id {email.id} with event_id {email.event_id}")

    except Exception as e:
        logger.error(f"Error in send_emails task: {e}")
