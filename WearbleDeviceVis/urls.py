"""WearbleDeviceVis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from VisApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('upload', views.upload, name = 'upload'),
    path('results_living', views.results_living, name = 'results_living'),
    path('results_threadmill', views.results_thread, name = 'results_thread'),
    path('renew', views.renew, name = 'renew'),
    path('renew_pread', views.renew_pread, name='renew_pread'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('compare', views.compare, name = 'compare'),
    path('renew_com_pread', views.renew_com_pread, name = 'renew_com_pread'),
    # path('compare_freeliving', views.compare_freeliving, name = 'renew_com_pread'),
    path('results_threadmill', views.results_thread, name = 'results_thread'),
    path('renew_com_living', views.renew_com_living, name = 'renew_com_living')
]
