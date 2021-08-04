"""Schema URL Configuration

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
from django.urls import path

import Schema
from login import urls as login_url
from createobject import urls as createobject_url
from MapSchema import urls as MapSchema_url
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(login_url)),
    path('create/', include(createobject_url)),
    path('map/',include(MapSchema_url))
]
