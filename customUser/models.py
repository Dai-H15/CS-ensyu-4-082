from django.db import models
from login.models import PersonalData
# Create your models here.


class CommunityModel(models.Model):
    community_name = models.CharField(max_length=30)
    community_Key = models.CharField(max_length=33, primary_key=True)
    introduce = models.CharField(max_length=300)
    is_RegistByEmail = models.BooleanField()


class CustomUserModel(models.Model):
    custom_user_Name = models.CharField(max_length=50)
    user_key = models.ForeignKey(PersonalData, on_delete=models.DO_NOTHING)
    custom_user_key = models.CharField(max_length=33, primary_key=True)
    Community = models.ForeignKey(CommunityModel, on_delete=models.DO_NOTHING)
