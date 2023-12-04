# chat/models.py
from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator



class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='chatrooms', blank=True)
    max_members = models.IntegerField(validators=[MaxValueValidator(10)], default=0)

    def __str__(self):
        return self.name

    # class Meta:
    #     unique_together = ['name', 'users']

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True)

