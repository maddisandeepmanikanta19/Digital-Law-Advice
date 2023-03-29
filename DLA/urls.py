"""DLA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from lawyer_signup.views import lawyersignupaction
from lawyer_login.views import lawyerloginaction
from lawyer_profile.views import lawyerprofileaction
from client_signup.views import clientsignupaction
from client_login.views import clientloginaction
from index.views import index
from lawyer_profile_update.views import lawyerprofileupdate
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index),
    path('lawyersignup/',lawyersignupaction,name="lawyersignup"),
    path('lawyerlogin/',lawyerloginaction,name="lawyerlogin"),
    path('lawyerprofile/',lawyerprofileaction,name="lawyerprofile"),
    path('lawyerprofileupdate/',lawyerprofileupdate,name="lawyerprofileupdate"),
    path('clientsignup/',clientsignupaction,name="clientsignup"),
    path('clientlogin/',clientloginaction,name="clientlogin"),
]

