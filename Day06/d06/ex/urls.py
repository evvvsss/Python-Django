from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='ex06-homepage'),
    # path('display/', views.Display.as_view(), name='ex05-display'),
    # path('remove/', views.Remove.as_view(), name='ex05-remove'),
]