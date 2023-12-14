from django.db import models
from login.models import PersonalData 
import secrets
from django.db.models.signals import post_save


class CommunityModel(models.Model):
    community_name = models.CharField(max_length=30)
    community_Key = models.CharField(max_length=33, primary_key=True)
    introduce = models.CharField(max_length=300)
    is_RegistByEmail = models.BooleanField()

    def __str__(self):
        return self.community_name


class CustomUserModel(models.Model):
    PersonalData = models.ForeignKey(PersonalData, on_delete=models.DO_NOTHING)
    custom_user_Name = models.CharField(max_length=50)
    custom_user_key = models.CharField(max_length=33, primary_key=True)
    Community = models.ForeignKey(CommunityModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.custom_user_Name


def CreateCommunity(sender, instance, created, **kwargs):
    if created:
        if not CommunityModel.objects.filter(community_name="Everyone").exists():
            data = CommunityModel()
            data.community_Key = secrets.token_hex(32)
            data.community_name = "Everyone"
            data.introduce = "みんなのコミュニティー"
            data.is_RegistByEmail = False
            data.save()


def CreateDefCustomUser(sender, instance, created, **kwargs):
    if created:
        data = CustomUserModel()
        data.PersonalData = instance
        data.custom_user_key = secrets.token_hex(32)
        data.custom_user_Name = instance.username
        data.Community = CommunityModel.objects.get(community_name="Everyone")
        data.save()


post_save.connect(CreateCommunity, sender=PersonalData)
post_save.connect(CreateDefCustomUser, sender=PersonalData)
