from django.db import models
from django.core.validators import RegexValidator, validate_email

# Create your models here.
class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(validators=[validate_email], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
