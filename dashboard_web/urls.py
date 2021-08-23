from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('ftp', views.ftp, name='ftp_overview'),
    path('endlessh', views.endlessh, name='endlessh_overview')
]
