from django.shortcuts import render

from django.http import JsonResponse

from .models import Customer



def get_all_customers(request, *args, **kwargs):                        # http://127.0.0.1:8000/customer/all/
    print('------------------------------------get_all_customers')
    customers = Customer.objects.all()
    json = []
    for c in customers:
        json.append({'name': c.name, 'profession': c.profession})

    return JsonResponse(json, safe=False)
