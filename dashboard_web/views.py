from django.shortcuts import render

from cool_api.models import FtpLogin, Endlessh


# Create your views here.

def index(request):
    ftp_logins = FtpLogin.get_10_latest()
    endlessh = Endlessh.get_10_latest()
    context = {'ftplogins' : ftp_logins, 'endlessh': endlessh}
    return render(request, "dashboard_web/index.html", context)


def ftp(request):
    ftp_logins = FtpLogin.get_all()
    context = {'ftplogins': ftp_logins}
    return render(request, "dashboard_web/ftp_overview.html", context)


def endlessh(request):
    endlessh = Endlessh.get_10_latest()
    context = { 'endlessh': endlessh }
    return render(request, "dashboard_web/endlessh_overview.html", context)

def test(request):
    return render(request, "dashboard_web/test.html")
