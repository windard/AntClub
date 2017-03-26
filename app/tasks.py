# coding=utf-8

import os
from flask import render_template
from flask_mail import Message
from flask_celery3 import make_celery

from app import mail, create_celery_app

celery_app = create_celery_app(os.getenv('XDANT_CELERY_CONFIG' or 'default'))
celery = make_celery(celery_app)


@celery.task(bind=True)
def send_email(self, to, subject, template, **kwargs):
    msg = Message(celery_app.config['XDANT_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=celery_app.config['XDANT_MAIL_SENDER'], recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)

    try:
        with celery_app.app_context():
            mail.send(msg)
    except Exception as e:
        raise self.retry(exc=e, countdown=10)
