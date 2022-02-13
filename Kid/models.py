from django.db import models
from phone_field import PhoneField
from django.utils.html import mark_safe

# Create your models here.
class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name

FOOD_GROUP = [
    ('Veg', 'Vegetarian'),
    ('Fruit', 'Fruit'),
    ('Grain', 'Grain'),
    ('Protein', 'Protein'),
    ('Dairy', 'Dairy'),
    ('Confectionery', 'Confectionery'),
    ('Unknown', 'Unknown'),
]

class Image(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image_url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100, blank=True)
    food_group = models.CharField(max_length=100, choices=FOOD_GROUP, default='Unknown')

    @property
    def image_preview(self):
        if self.image_url:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image_url))
        return ""
    