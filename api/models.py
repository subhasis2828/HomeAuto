from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    deviceId    = models.CharField(max_length=10,primary_key=True)
    deviceType  = models.CharField(max_length=20)
    lightStatus = models.IntegerField(choices=((0,0),(1,1)),default=0)
    fanStatus   = models.IntegerField(choices=((0,0),(1,1)),default=0)


    def __str__(self):
        return self.deviceId

class UserDevice(models.Model):
    user   = models.ForeignKey(User,on_delete=models.CASCADE)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' ' + self.device.deviceId

