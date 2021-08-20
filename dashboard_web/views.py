from django.shortcuts import render

from .models import Test


# Create your views here.


def dashboard(request):
    test = request.GET.dict()
    name = test['name']
    data = Test.objects
    return render(request, "dashboard_web/dashboard.html", {"PETER": "COOL", "NAME": data})