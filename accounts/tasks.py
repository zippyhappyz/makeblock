from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_html_email(subject, recipient_list, template, context):
    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject, text_content, 'makeblock.education@smart-generation.kz', recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


@shared_task
def send_new_student_email(user_pk, password):
    user = get_user_model().objects.get(pk=user_pk)
    send_html_email(
        subject="Подтверждение и учетные данные вашей учетной записи MBE LMS",
        recipient_list=[user.email],
        template="accounts/email/new_student_account_confirmation.html",
        context={"user": user, "password": password},
    )


@shared_task
def send_new_lecturer_email(user_pk, password):
    user = get_user_model().objects.get(pk=user_pk)
    send_html_email(
        subject="Подтверждение и учетные данные вашей учетной записи MBE LMS",
        recipient_list=[user.email],
        template="accounts/email/new_lecturer_account_confirmation.html",
        context={"user": user, "password": password},
    )