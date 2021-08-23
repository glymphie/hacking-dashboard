from django.shortcuts import render

from cool_api.models import FtpLogin, Endlessh


# Create your views here.

def index(request):
    ftp_logins = FtpLogin.get_10_latest()
    endlessh = Endlessh.get_10_latest()
    context = {'ftplogins' : ftp_logins, 'endlessh': endlessh}
    return render(request, "dashboard_web/index.html", context )


def ftp(request):
    return render(request, "dashboard_web/ftp_overview.html")


def endlessh(request):
    return render(request, "dashboard_web/endlessh_overview.html")
