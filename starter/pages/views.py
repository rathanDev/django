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


def dashboard_view(request, *args, **kwargs):
    my_context = {
        "my_text": "my_text",
        "my_number": 123,
        "my_list": [1,2,3,4]
    }
    return render(request, "dashboard.html", my_context)