import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


logr = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance'))
        logr.debug("UserProfile created: %s" % up)