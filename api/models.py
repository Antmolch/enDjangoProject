import uuid

from django.db import models
from django.contrib.auth.models import User



class Bot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    login_id = models.ForeignKey(User, max_length=255, default=None, on_delete=models.CASCADE)
    unique_name = models.CharField(max_length=255, default=None)
    name = models.CharField(max_length=255, default=None)
    token = models.CharField(max_length=255, default=None)
    url = models.CharField(max_length=255, default=None)
    launch_status = models.BooleanField(max_length=255,default=None)

    def __str__(self):
        return self.name

class TypeCommand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =  models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name

class Command(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bot_id = models.ForeignKey(Bot, on_delete=models.CASCADE)
    type_id = models.ManyToManyField(TypeCommand)
    name = models.CharField(max_length=255,default=None)
    link_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CommandCall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    command_id = models.ForeignKey(Command, on_delete=models.CASCADE,related_name='calls')
    name = models.CharField(max_length=255,default=None)

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    command_id = models.OneToOneField(Command, on_delete=models.CASCADE,related_name='media')
    name = models.CharField(max_length=255,default=None)
    type = models.CharField(max_length=255,default=None)
    file = models.TextField()
