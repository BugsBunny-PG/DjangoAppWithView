from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request): #request is a http requeat object
    
    return HttpResponse('<h1>Hello django</h1>')