from django.db import models
# Create your models here.
class NodeRegistration(models.Model):
    ipAddress = models.CharField(max_length=32)
    couchReplication = models.BooleanField()
    ipfsReplication = models.BooleanField()

class UserRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    publicKey = models.TextField(unique=True)