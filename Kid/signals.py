from django.dispatch import receiver
from django.shortcuts import render
from .models import Kid, Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

@receiver(post_save, sender=Image)
def validate_group(sender, instance, created, **kwargs):
    if instance.food_group == 'Unknown':
        template = render_to_string('email_template.html', {'name': instance.kid.name, 'image': instance.image_url})
        email = EmailMessage(
            subject='Image does not contain food',
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=[instance.kid.email_address],
        )
        email.fail_silently = False
        email.send()
