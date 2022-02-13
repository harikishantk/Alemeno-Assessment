from django.db import models
from phone_field import PhoneField

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
    approved_by = models.CharField(max_length=100, blank=False)
    food_group = models.CharField(max_length=100, choices=FOOD_GROUP, default='Unknown')