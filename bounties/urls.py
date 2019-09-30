from django.urls import path
from . import views

urlpatterns = [
    path('', views.bounty_list, name='bounty_list')
]