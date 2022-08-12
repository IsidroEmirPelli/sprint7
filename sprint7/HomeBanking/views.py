from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'HomeBanking/index.html')


def dashboard(request):
    return render(request, 'HomeBanking/dashboard.html')


def dollar(request):
    return render(request, 'HomeBanking/dollar.html')
