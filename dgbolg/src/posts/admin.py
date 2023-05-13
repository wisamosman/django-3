from django.contrib import admin

# Register your models here.
from .models import post, author

admin.site.register(post)
admin.site.register(author)