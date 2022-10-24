from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('index',views.index,name='index'),
    path('form',views.form,name='form'),
    path('table',views.table,name='table'),
    path('signup',views.signup,name='signup'),

]
