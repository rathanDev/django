from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hellow Django!!</h1>") 

def contact_view(*args, **kwargs):
    return HttpResponse("<h2>Contact Page</h2>")