from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)   #integrates Posts in admin site

admin.site.register(Comment)
