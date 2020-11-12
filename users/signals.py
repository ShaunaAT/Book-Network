from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Library

@receiver(post_save, sender=User)
def create_user_stuff(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Library.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_stuff(sender, instance, **kwargs):
    instance.profile.save()
    instance.library.save()
    

