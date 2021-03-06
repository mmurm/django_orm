"""django_orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^users/', include('apps.Users.urls')),
    url(r'^dojo/', include('apps.dojo_ninja.urls')),
    url(r'^b_a/', include('apps.books_author.urls')),
    url(r'^shows/', include('apps.shows.urls')),
    url(r'^l_r/', include('apps.l_r.urls')),
    url(r'^wall/', include('apps.wall.urls')),
    url(r'^fav_b/', include('apps.fav_book.urls')),
]
