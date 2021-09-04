from django.shortcuts import render

#from http import HttpResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
# Create your views here.
