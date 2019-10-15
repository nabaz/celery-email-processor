from celery import Celery
from celery import task  
from django.core.mail.message import EmailMessage
from django.core.files.storage import default_storage
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
logger = get_task_logger(__name__)

# @periodic_task(
#     run_every=(crontab(minute='*/20')),
#     name="send_email",
#     ignore_result=True
# )
@task(name="Sending Email")
def send_email():
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    email = SendEmail('nabaz.maaruf@aenetworks.com', ['nabaz@outlook.com,'], 'Hello', 'Hey hey hey')
    
    return SendEmail.handler(email)

import boto3

class SendEmail:

    def __init__(self, email_from, email_to, email_subject, email_body):

        self.email_from = email_from
        self.email_to = email_to
        self.email_subject = email_subject
        self.email_body = email_body

        self.ses = boto3.client('ses')

    def handler(self):
        response = self.ses.send_email(
            Source = self.email_from,
            Destination={
                'ToAddresses': self.email_to,
            },
            Message={
                'Subject': {
                    'Data': self.email_subject
                },
                'Body': {
                    'Html': {
                        'Data': self.email_body
                    }
                }
            }
        )
        
        return response
