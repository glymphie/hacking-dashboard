from django.shortcuts import render

# from .models import Test

from cool_api.models import FtpLogin, Endlessh


# Create your views here.


def dashboard(request):
    ftp_logins = FtpLogin.get_all()
    endlessh = Endlessh.get_all()
    context = {'ftplogins' : ftp_logins, 'endlessh': endlessh}
    return render(request, "dashboard_web/dashboard.html", context )
