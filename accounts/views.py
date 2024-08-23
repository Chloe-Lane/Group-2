from django.shortcuts import render
from .forms import RegisterForm, User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password')
    password2 = form.cleaned_data.get('password2')

    newUser = User.objects.create_user(username, email, password)
    return render(request, 'auth/register.html', context)
