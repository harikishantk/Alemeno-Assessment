from django.dispatch import receiver
from .models import Kid, Image
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Image)
def validate_group(sender, instance, created, **kwargs):
    if instance.food_group == 'Unknown':
        # send mail
