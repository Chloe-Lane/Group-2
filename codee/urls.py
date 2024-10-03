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
from tweets.views import home
from accounts import views as account_views
from . import views
from .views import page_view

# Import View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tweet/', include('tweets.urls')),
    path('accounts/', include('accounts.urls')),
    path('register/', account_views.register, name='register'),
    path('register/', views.register_view, name='register_view_name'),
    path('login/', views.login_view, name='login_view_name'),
    path('page/', views.page_view, name='page_view_name'),
    path('captcha/', include('captcha.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
