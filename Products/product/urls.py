from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('apost/', views.AdminCreatePost.as_view(), name='apost'),
    path('alistalltise/', views.ListAllTise.as_view(), name='alistalltise'),
    path('adpost/<int:pk>', views.ADeletePost.as_view(), name='adpost'),
    path('logout/', views.logoutView, name='logout'),

]
