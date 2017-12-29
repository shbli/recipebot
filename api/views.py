from django.shortcuts import render
from django.http import HttpResponse
from json import dumps


# Create your views here.
def index(request):
    return HttpResponse(dumps({ 'message': 'Welcome home'}))