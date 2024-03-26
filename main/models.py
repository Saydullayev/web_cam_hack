from django.db import models

class user(models.Model):
    chat_id = models.CharField(max_length=100)