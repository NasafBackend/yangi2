
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="homepage"),
    path('send/', views.send, name="homepage" ),
]