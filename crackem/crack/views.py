from django.shortcuts import render, redirect

from crackem.crack.forms import RegistrationForm
from crackem.crack.models import User


# Create your views here.

def index(request):
    return render(request, 'common/index_page(home).html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            user = User.objects.create(username=username, password=password, first_name=first_name,
                                       last_name=last_name, email=email)
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'authorize_folder/register.html', context)


def login(request):
    return render(request, 'authorize_folder/login.html')
