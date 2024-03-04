from flask_mail import Message
from app import mail


def send_email(to, subject, content):
    try:
        message = Message(subject=subject, recipients=[to], body=content)
        mail.send(message)

        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False
