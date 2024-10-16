import string, random
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages



def generate_captcha(request):
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    request.session['captcha'] = captcha_text  # Save the CAPTCHA text in the session

    # Create CAPTCHA image
    img = Image.new('RGB', (250, 80), color='white')
    d = ImageDraw.Draw(img)

    # Set font size and load a font
    font_size = 30  # Increase font size here
    try:
        # Load a font (you may need to provide the correct path to a .ttf file)
        font = ImageFont.truetype("arial.ttf", font_size)  # Adjust font size and type as needed
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if specific font cannot be loaded

    # Draw the text with the specified font
    d.text((10, 20), captcha_text, fill=(0, 0, 0), font=font)

    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


last_registered_email = ""
last_registered_password = ""
last_registered_first_name = ""
last_registered_last_name = ""


def home(request):
    global last_registered_email, last_registered_password, last_registered_first_name, last_registered_last_name, hide_last_name

    if request.method == 'POST':
        if request.POST['captcha'] != request.session['captcha']:
            messages.error(request, 'INvalid captcha')
            return render(request, 'auth/home.html')  # Re-render the page with error message
        else:
            last_registered_email = request.POST['email']
            last_registered_password = request.POST['password']
            last_registered_first_name = request.POST['first_name']  # Capture first name
            last_registered_last_name = request.POST['last_name']  # Capture last name

            # Check if the "hide last name" checkbox is checked
            hide_last_name = request.POST.get('hide_last_name') is not None  # Set to True if checked, False otherwise
            request.session['hide_last_name'] = hide_last_name  # Store in session

            username = last_registered_email.split('@')[0]  # Extract the username from the email

            # Check if the username already exists
            while User.objects.filter(username=username).exists():
                username += str(random.randint(1, 1000))  # Append a random number if the username exists

            # Create a new user with the provided email, password, and username
            User.objects.create_user(username=username, email=last_registered_email, password=last_registered_password)

            # Redirect to the login page after registration
            return redirect('login')

    return render(request, 'auth/home.html')


def login_view(request):
    global last_registered_email, last_registered_password, last_registered_first_name, last_registered_last_name  # Access the global variables

    error = None  # Initialize the error variable

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email and password match the last registered user's credentials
        if email == last_registered_email and password == last_registered_password:
            return redirect('page', first_name=last_registered_first_name, last_name=last_registered_last_name)  # Pass parameters
        else:
            error = 'Invalid email or password'  # Set error if credentials don't match

    # Render the login page with the error message if it exists
    return render(request, 'auth/login.html', {'error': error})


def custom_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page

def page_view(request, first_name, last_name):
    hide_last_name = request.session.get('hide_last_name', False)  # Retrieve from session or use a default

    return render(request, 'homep/page.html', {
        'first_name': first_name,
        'last_name': last_name,
        'hide_last_name': hide_last_name,
    })


import time
timestamp = int(time.time())


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')