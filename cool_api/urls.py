from django.urls import path

from . import views

urlpatterns = [
    path('ftp-login', views.ftp_login, name='ftp-login', )
]
