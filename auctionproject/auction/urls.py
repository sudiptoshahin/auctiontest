from django.contrib import admin
from django.conf.urls import url, include
from main import views as main_views
from auction import views


urlpatterns = [

    url(r'^$', main_views.home, name='home'),


    # auction features url
    url(r'^dashboard/auction/items/$', views.show_auction_items, name='dashboard_auction_item'),
    url(r'^auction/add/item/$', views.add_item, name='add_auction_item'),
]