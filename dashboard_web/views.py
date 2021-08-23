from django.shortcuts import render

from cool_api.models import FtpLogin, Endlessh


# Create your views here.

def index(request):
    context = {
        'ftplogins' : FtpLogin.get_10_latest(),
        'endlessh': Endlessh.get_10_latest(),
        'counter_ftp': FtpLogin.get_counters(),
        'counter_endlessh': Endlessh.get_counters()
    }
    return render(request, "dashboard_web/index.html", context)


def ftp(request):
    context = {'ftplogins': FtpLogin.get_all()}
    return render(request, "dashboard_web/ftp_overview.html", context)


def endlessh(request):
    context = { 'endlessh': Endlessh.get_all() }
    return render(request, "dashboard_web/endlessh_overview.html", context)

def test(request):
    return render(request, "dashboard_web/test.html")
