from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User

@csrf_exempt
def get_all_users(request, *args, **kwargs):
    print('-----------------get_all_users')
    users = User.objects.all()
    json = []
    for u in users:
        json.append({'name': u.name, 'profession': u.profession})

    return JsonResponse(json, safe=False)