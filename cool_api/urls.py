from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'ftp-login', views.FtpLoginViewSet)
router.register(r'endlessh-login', views.EndlesshViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ftp-login/', include('rest_framework.urls', namespace='rest_framework_ftp-login')),
    path('endlessh-login/', include('rest_framework.urls', namespace='rest_framework_endlessh')),
]
