from django.contrib import admin
from .models import *

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('chat_id',)