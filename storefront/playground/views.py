from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request --> response
# request handler 

    # Pull data from db
    # Transform 
    # Send email

def say_hello(request):
    # return HttpResponse('Hello World')
    x = 1
    y = 1
    return render(request, 'hello.html', {'name': 'Rathan'})