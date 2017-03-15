"""app URL Configuration

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

from shop import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.CategoryList.as_view(), name='index'),
    url(r'^xxx$', views.xxx, name='xxx'),
    url(r'^(?P<pk>\d*)/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<category_id>\d*)/add_item/$', views.add_item, name='add_item'),
    url(r'^item/(?P<pk>\d*)/$', views.ItemFormView.as_view(), name='item'),
]
