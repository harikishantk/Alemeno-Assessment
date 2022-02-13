from django.contrib import admin
from .models import Kid, Image

# Register your models here.
admin.site.register(Kid)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview
    
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

admin.site.register(Image, ImageAdmin)