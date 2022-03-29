from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.TextField(max_length=100,blank=True)
    location = models.TextField(max_length=20,blank=True)
    photo = models.ImageField(upload_to='dp',default='dp/default.jpg')

    def __str__(self):
        return self.user.username +" 's profile"

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()


