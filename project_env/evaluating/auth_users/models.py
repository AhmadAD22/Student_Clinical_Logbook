from django.db import models 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import *
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)





class UserProfile(models.Model):

    user_name = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    user_id=  models.PositiveIntegerField(unique=True)
    def __str__(self):
        return str(self.user_id)+' : '+self.user_name.username



    