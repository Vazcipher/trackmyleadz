from django.core.mail import send_mail
from django.conf import settings

def sendMail(subject, message, toList):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        toList,
        fail_silently=False,
    )