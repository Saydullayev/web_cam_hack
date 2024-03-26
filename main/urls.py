from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('free_diamond/<user_id>', free_diamon),
]
