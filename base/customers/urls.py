from django.contrib import admin
from django.urls import path, include

from . import views

# -----

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path('all/', views.get_all_customers, name='get_all_customers'),

    # -----

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
