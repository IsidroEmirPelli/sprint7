from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'HomeBanking/index.html')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'HomeBanking/dashboard.html')


def dollar(request):
    return render(request, 'HomeBanking/dollar.html')
