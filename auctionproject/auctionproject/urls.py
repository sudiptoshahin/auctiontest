from django.contrib import admin
# from django.conf.urls import url, include
from django.urls import re_path, include

urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path(r'^admin/$', admin.site.urls),

    # main app
    re_path(r'', include('main.urls')),


]
