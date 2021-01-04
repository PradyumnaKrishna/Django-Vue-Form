import os, time
from django.db import models
from django.dispatch import receiver
from django.core.validators import RegexValidator, validate_email
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(email, name):
    ID = 'd-42e1f10c6ddb46d2ac32ae1277568c96'
    sender='test@mail.pradyumna.me'
    receivers = [(email, name)]
    
    message = Mail(
        from_email=sender,
        to_emails=receivers)

    message.template_id = ID

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)

        # code, body, headers = response.status_code, response.body, response.headers
        # print(f"Response code: {code}")
        # print(f"Response headers: {headers}")
        # print(f"Response body: {body}")
        # print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))
    return str(response.status_code)


# Create your models here.
class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(validators=[validate_email], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)

@receiver(models.signals.post_save, sender=Form)
def execute_after_save(sender, instance, created, **kwargs):
    if created:
        send_email(instance.email, instance.name)
