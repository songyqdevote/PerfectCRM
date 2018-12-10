
from django.urls import path
from crm import views
urlpatterns = [
    path('', views.index),
]