from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers



from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('all/', views.get_all_customers, name='get_all_customers'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('hello/', views.HelloView.as_view(), name='hello'),

]
