"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from app import views
#from drinks import views
#import debug_toolbar
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls), 
    #path('',views.index),
    #path('register',views.register),
    path('',views.hug),
    #path('',views.hello),
    #path('__debug__/', include('debug_toolbar.urls')),
    #path('drinks/',views.drinks_list),
    #path('drinks/<int:id>',views.drink_detail),
    #path('movies/<int:movie_id>',views.movie)
]
#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
     ]