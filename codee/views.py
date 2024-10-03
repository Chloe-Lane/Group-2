from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

def home(request):
    return render(request, 'auth/home.html')  # Render the appropriate template

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Handle successful registration
            return redirect('success_page')
        else:
            # If the form is invalid, including CAPTCHA, it will regenerate a new CAPTCHA image automatically.
            pass
    else:
        form = RegistrationForm()
    return render(request, 'auth/home.html', {'form': form})


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_view_name')  # Redirect to login page after successful registration
        except Exception as e:
            messages.error(request, str(e))

    return render(request, 'auth/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user
            return redirect('login_view_name')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'auth/home.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Adjust based on your User model

        if user is not None:
            auth_login(request, user)
            return redirect('page_view_name')  # Redirect to the page view
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'auth/login.html')


def page_view(request):
    return render(request, 'homep/page.html')  # Adjust path if necessary

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the registration (e.g., save user data)
            return redirect('success_view_name')  # Redirect on successful registration
        else:
            # If CAPTCHA or other validation fails, re-render the form with errors
            return render(request, 'auth/home.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'auth/home.html', {'form': form})