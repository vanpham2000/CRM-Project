"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from landingpage.views import (
    VerifyAccount,
    nav,
    register,
    welcome,
    AccessDenied,
    Error,
    CustomerAccounts

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', VerifyAccount , name='userlogin'),
    path('', nav , name='welcome_page'),
    path('register123/', register, name="register"),
    path('welcome/<str:user_identifier>/', welcome, name='welcome'),
    path('welcome/<str:user_identifier>/customers/', CustomerAccounts, name='customeraccount'),
    path('<path:catch_all>/',Error, name='catch_all_error'),
    path('accessdenied', AccessDenied, name='accessdenied'),


]
