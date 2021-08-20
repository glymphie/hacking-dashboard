from django.shortcuts import render
from django.http import HttpResponse

from .models import FtpLogin

# Create your views here.

def ftp_login(request):
    if request.method == 'POST':
        test = request.POST
        print(test)
    return HttpResponse()
