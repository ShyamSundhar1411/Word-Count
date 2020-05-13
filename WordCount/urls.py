
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='count'),
    path('about/',views.absts,name='abt')
]
