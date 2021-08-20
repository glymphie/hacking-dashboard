from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .models import FtpLogin
from .serializers import FtpLoginSerializer

# Create your views here.

class FtpLoginViewSet(viewsets.ModelViewSet):
    queryset = FtpLogin.objects.all().order_by('date')
    serializer_class = FtpLoginSerializer
