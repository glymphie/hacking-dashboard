from django.shortcuts import render

# from .models import Test

from cool_api.models import FtpLogin


# Create your views here.


def dashboard(request):
    dblogins = FtpLogin.get_all()
    context = {'ftplogins' : dblogins}
    return render(request, "dashboard_web/dashboard.html", context )
