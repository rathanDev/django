from django.shortcuts import render

from django.http import JsonResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, GroupSerializer

from .models import Customer



def get_all_customers(request, *args, **kwargs):                        # http://127.0.0.1:8000/customer/all/
    print('------------------------------------get_all_customers')
    customers = Customer.objects.all()
    json = []
    for c in customers:
        json.append({'name': c.name, 'profession': c.profession})

    return JsonResponse(json, safe=False)





class UserViewSet(viewsets.ModelViewSet):
    print('UserViewSet------------------------------------------')
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]






