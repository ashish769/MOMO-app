from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='index'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('register/',Register,name='register'),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    #for change password//bracket vitra ko template haru hataune
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
]
