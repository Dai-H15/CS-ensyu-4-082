from django.db import models
from django.contrib.auth.models import User
import secrets
from django.db.models.signals import post_save


class PersonalData(models.Model):
    username = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    birth = models.DateField(default="1990-01-01")
    phone = models.CharField(max_length=20)
    user_key = models.CharField(max_length=33)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_key


def CreatePersonalData(sender, instance, created, **kwargs):
    if created:
        data = PersonalData(user=instance)
        data.username = instance.username
        data.FirstName = instance.first_name
        data.LastName = instance.last_name
        data.user_key = secrets.token_hex(32)
        data.email = instance.email
        data.save()
    else:
        data = PersonalData.objects.get(user=instance)
        data.username = instance.username
        data.FirstName = instance.first_name
        data.LastName = instance.last_name
        data.email = instance.email
        data.save()


post_save.connect(CreatePersonalData, sender=User)

# Create your models here.
