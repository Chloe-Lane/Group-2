"""
URL configuration for codee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home,
    login_view,
    custom_logout,
    page_view,
    generate_captcha,
    forgot_password_view,
    send_reset_code,
    reset_password,
    send_verification_code,
    verify_code,
)
from .views import *
from django.contrib.auth import views as auth_views

# Import View

# Import View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('tweet/', include('tweets.urls')),
    path('page/<str:first_name>/<str:last_name>/', page_view, name='page'),
    path('logout/', custom_logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    path('generate_captcha/', generate_captcha, name='generate_captcha'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('send-reset-code/', send_reset_code, name='send_reset_code'),
    path('reset-password/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('forgot-password/', send_reset_code, name='send_reset_code'),
    path('send-verification-code/', send_verification_code, name='send_verification_code'),
    path('verify-code/', verify_code, name='verify_code'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
