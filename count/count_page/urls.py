from django.urls import path
from . import views

urlpatterns=[
  path('',views.counter),
  path('add_two', views.add_two),
  path('clear',views.clear),
]