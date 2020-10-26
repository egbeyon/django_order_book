from django.urls import path

from . import views

urlpatterns= [
    path('clicked', views.clicked, name= 'clicked')
]