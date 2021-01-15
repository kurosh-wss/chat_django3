from celery import shared_task
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

from django.contrib.auth.models import User

@shared_task
def user_registered(user_id):
    user = User.objects.get(id=user_id)
    to_email = user.email

    mail_subject = 'Activate your account.'

    message = render_to_string(
        'users/active_email.html', {
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
    })

    mail_sent = send_mail(subject=mail_subject, message=message, from_email=None, recipient_list=[to_email])
    print(mail_sent)

    return mail_sent
