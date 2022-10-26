from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('index',views.index,name='index'),
    path('form',views.form,name='form'),
    path('signup',views.signup,name='signup'),
    path('logout',views.user_logout,name='logout'),
    path('search/', views.index, name='index'),
    path('search/<str:search_query>/', views.search_result, name='search'),

]
