"""MySite101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from . import views # 1

urlpatterns = [
    path('', views.index),# call the index function of views.py file. # blank url # 2
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3_1/', include('app3_1.urls')),
    path('app3_2/', include('app3_2.urls')),
    path('app4_0/', include('app4_0.urls')),
    path('app4_1/', include('app4_1.urls')),
    path('app4_2/', include('app4_2.urls')),
    path('app4_3/', include('app4_3.urls')),
    path('app5_1/', include('app5_1.urls')),
    # 6. Database Configuration & Migration
    path('app6_1/', include('app6_1.urls')),
    # 7. Admin Site - Create Super User and Login
    path('admin/', admin.site.urls),# Add Admin Site
    path('app8_1/', include('app8_1.urls')),
    path('app9_1/', include('app9_1.urls')),
]