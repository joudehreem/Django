from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random_number', views.random_number),
    path('again', views.again, name='again'),
]
