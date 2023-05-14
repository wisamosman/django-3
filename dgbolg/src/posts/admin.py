from django.contrib import admin

# Register your models here.
from .models import post, author

class postAdmin(admin.ModelAdmin):
    list_display = ['title' ,'author', 'publish_date']
    list_filter = ['author','tags','publish_date']

admin.site.register(post,postAdmin)
admin.site.register(author)