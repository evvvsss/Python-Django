from django.urls import path
from ex02 import views



urlpatterns = [
    path('init/', views.init, name='ex03-init'),
    path('populate/', views.populate, name='ex03-populate'),
    path('display/', views.display, name='ex03-display'),
]