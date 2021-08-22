from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ftp', views.ftp, name='ftp_overview'),
    path('endlessh', views.endlessh, name='endlessh_overview')

]
