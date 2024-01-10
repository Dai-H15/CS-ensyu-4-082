from django.db import models
 
# Create your models here.

class ChatRoomModel(models.Model):
    chat_room_key = models.CharField(max_length=70)
    chat_data = models.JSONField()
