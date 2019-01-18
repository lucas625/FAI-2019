from django.contrib import admin
from .models import LikePost, LikeThread

admin.site.register(LikePost)
admin.site.register(LikeThread)
