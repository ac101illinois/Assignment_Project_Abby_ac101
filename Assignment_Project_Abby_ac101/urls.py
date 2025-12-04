"""
URL configuration for Assignment_Project_Abby_ac101 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from students.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls', namespace='students')),

    # Login view
    path('login/',
         LoginView.as_view(template_name='login.html'),
         name='login_urlpattern'),

    # Logout view
    path(
        'logout/',
        LogoutView.as_view(next_page='students:home'),
        name='logout_urlpattern'
    ),
    # Signup view
    path('signup/',
         signup_view,
         name='signup_urlpattern'),
]