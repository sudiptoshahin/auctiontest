from django.contrib import admin
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^auction/$', views.home, name='home'),

    url(r'^auction/add/item/$', views.add_item, name='add_auction_item'),
]