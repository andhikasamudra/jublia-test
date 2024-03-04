# app/celery_worker.py
from celery import Celery
import os


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    celery.conf.update(
        CELERY_APP=os.environ.get("CELERY_APP", "app.celery_worker.celery")
    )

    return celery


celery = make_celery(app)
