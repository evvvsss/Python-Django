from django.urls import path

from ex01 import views



urlpatterns = [
    path('', views.init, name='ex01-init'),
]