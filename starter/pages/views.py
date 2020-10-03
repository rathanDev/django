from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {}) 

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(*args, **kwargs):
    return HttpResponse("<h2>Contact Page</h2>")