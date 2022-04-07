# from django.conf.urls import url # For Django < 4.0
from django.urls import re_path # For Django >= 4.0
from main import views


urlpatterns = [

    re_path(r'^$', views.home, name='home'),

    re_path(r'^about/$', views.about, name='about'),
]