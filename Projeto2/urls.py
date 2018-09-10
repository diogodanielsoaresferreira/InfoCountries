"""Projeto2 URL Configuration

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
from django.conf.urls import url
import django.contrib.auth.views
from datetime import datetime

import app.forms
import app.views
from django.contrib import admin

urlpatterns = [
    url(r'^$', app.views.home, name="home"),
    url(r'^predicates/', app.views.predicates, name="pred"),
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^registar/$', app.views.registar, name="registar"),
    url(r'^country/(?P<country>[0-9]+)/favo$', app.views.changeFavorite, name="changeFavorite"),
    url(r'^country/(?P<country>[0-9]+)$', app.views.country, name="country"),
    url(r'^country/(?P<country>[0-9]+)/reload$', app.views.reload, name="reload"),
    url(r'^country/(?P<country>[0-9]+)/relations', app.views.relations, name="relations"),
    url(r'^metric/(?P<metric>[A-Z]?[0-9]+)$', app.views.metric, name="metric"),
    url(r'^inferences/(?P<success>success)?$', app.views.inferences, name="inferences"),
    url(r'^inferences/save$', app.views.saveinferences, name="saveinferences"),
    url(r'^favorites/$', app.views.favorites, name="favorites"),
    url(r'^statistics/$', app.views.statistics, name="statistics"),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'extra_context':
            {
                'title': 'Sign in with your account',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
