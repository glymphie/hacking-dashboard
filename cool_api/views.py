#from django.shortcuts import render
#from django.http import HttpResponse

from rest_framework import viewsets

from .models import FtpLogin, Endlessh
from .serializers import FtpLoginSerializer, EndlesshSerializer

# Create your views here.

class FtpLoginViewSet(viewsets.ModelViewSet):
    queryset = FtpLogin.objects.all().order_by('date')
    serializer_class = FtpLoginSerializer

class EndlesshViewSet(viewsets.ModelViewSet):
    queryset = Endlessh.objects.all().order_by('date')
    serializer_class = EndlesshSerializer
