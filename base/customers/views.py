from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Customer

@csrf_exempt
def get_all_customers(request, *args, **kwargs):
    print('------------------------------------get_all_customers')
    customers = Customer.objects.all()
    json = []
    for c in customers :
        json.append({'name': c.name, 'profession': c.profession})

    return JsonResponse(json, safe=False)
