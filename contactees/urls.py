from django.urls import path

from . import views

urlpatterns= [
    path('contactee', views.contactee, name= 'contactee')
]