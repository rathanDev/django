from django.shortcuts import render

from django.http import JsonResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, GroupSerializer

from .models import Customer

# -----

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



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






class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, there!'}
        return Response(content)


# curl -X POST -d "username=jana&password=jana@123" http://localhost:8000/api-token-auth/

# curl -H "Authorization: JWT "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImphbmEiLCJleHAiOjE2MTE2MzI0MDYsImVtYWlsIjoicmF0aGFuLmtwYXJhbUBnbWFpbC5jb20ifQ.oYET2CDPZIGq0AzdHbvdYhQf9y4XVXCQy6j0mqrjYTM" http://localhost:8000/customers/hello


