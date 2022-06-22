from textwrap import indent
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from premiosplatzi.premiosplatziapp.polls.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls"))
]
