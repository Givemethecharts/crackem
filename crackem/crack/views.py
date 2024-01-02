from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'common/index_page(home).html')


def register(request):
    return render(request, 'authorize_folder/register.html')


def login(request):
    return render(request, 'authorize_folder/login.html')
