from django.contrib import admin
from .models import Post
from .models import DestinationItem
from .models import UMKMProduct

# Register your models here.
admin.site.register(Post)

@admin.register(DestinationItem)
class DestinationItemAdmin(admin.ModelAdmin):
    list_display = ('deskripsi',)

@admin.register(UMKMProduct)
class UMKMProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_image', 'shopee_link')
    list_filter = ('price',)
    search_fields = ('name',)

    def display_image(self, obj):
        return f'<img src="{obj.image.url}" width="50" height="50" />'
    display_image.short_description = 'Image'
    display_image.allow_tags = True