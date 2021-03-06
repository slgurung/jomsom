"""jomsomProject URL Configuration

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
from django.conf.urls import url, include
#from django.urls import path

from django.contrib import admin
from posts import views

urlpatterns = [
    #path('', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    #url(r'^ghar/', admin.site.urls), #for security reason
    #path('admin/', admin.site.urls), # change r'^admin/' to something little random for security
    url(r'^admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    url(r'^accounts/', include('accounts.urls')),
    # 1.11 version
    url(r'^posts/', include('posts.urls')),


]
