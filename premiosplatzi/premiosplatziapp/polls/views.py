from this import d
from turtle import ht
from zlib import decompressobj
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")