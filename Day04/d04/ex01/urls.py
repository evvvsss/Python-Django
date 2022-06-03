from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('django/', django),
    path('display/', display),
    path('templates/', templates),
]
