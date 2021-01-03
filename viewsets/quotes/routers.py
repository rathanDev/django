from .viewsets import QuoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quotes', QuoteViewSet)