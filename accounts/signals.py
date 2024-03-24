from django.db.models.signals import post_save 
from django.dispatch import receiver 
from .models import UserProfile
from django.contrib.auth.models import User


@receiver(post_save ,sender=User,dispatch_uid="create_user_profile")
def create_userprofile(sender,instance, **kwargs):
    if UserProfile.objects.filter(user=instance).count()==0:
        UserProfile.objects.create(user=instance)