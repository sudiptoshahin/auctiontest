from unicodedata import name
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
# from django.urls import re_path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),

    url(r'^admin/', admin.site.urls),

    # main app
    url(r'', include('main.urls')),

    # auction
    url(r'', include('auction.urls')),


    # auth-sec
    url(r'^register/$', user_views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='front/login.html'), name='login'),
    url(r'^profile/$', user_views.profile, name='profile'),
    # url(r'^logout/', auth_views.LogoutView.as_view('front/logout.html'), name='logout'),


]

if settings.DEBUG == True:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


