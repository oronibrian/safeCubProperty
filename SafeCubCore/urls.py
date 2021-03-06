"""SafeCubCore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.urls import include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='main/', permanent=True)),
    path('main/', include('tenants.urls')),
    path('property/', include('property.urls')),

    path('accounts/logout/',LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    # path('accounts/login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),

    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('accounts/', include('django.contrib.auth.urls')), # new

]

admin.site.site_header = 'SafeCub Property administration'

