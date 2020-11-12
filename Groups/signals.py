from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import GroupList

@receiver(post_save, sender=User)
def create_grouplist(sender, instance, created, **kwargs):
    if created:
        GroupList.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_grouplist(sender, instance, **kwargs):
    instance.grouplist.save()
    