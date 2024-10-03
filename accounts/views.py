from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Perform your registration logic here.
            messages.success(request, "Registration successful!")
            return HttpResponse("Registration successful!")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'auth/home.html', {'form': form})



