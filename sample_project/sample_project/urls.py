"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django_app.views import *
urlpatterns = [
    url(r'^admin/',        include(admin.site.urls)),
    url(r'^accounts/',     include('allauth.urls')),
    url(r'^$',             indexpage, name = 'indexpage'),
    url(r'^login/',        login, name = 'login'),
    url(r'^yuvashakti/',   login, name = 'login'),
    url(r'^index/',        profilepage, name = 'profilepage'),
    url(r'^birthdaywish/', makewish, name = 'makewish'),
    url(r'^upload/',       upload_file, name = 'upload_file'),
    url(r'^videos/',       videos, name = 'videos'),
    url(r'^inbox/',        desplay_message, name = 'desplay_message'),
    url(r'^delete/(?P<id>\d+)/$', messageDelete, name='messagedelete'),
    #url(r'^checkout/(?P<id>\d+)$',                           OrderCheckout.as_view(),   name="order_checkout"),
    url(r'^biography/',    biography, name = 'biography'),
    url(r'^lockscreen/',   login, name = 'logout'),
]
