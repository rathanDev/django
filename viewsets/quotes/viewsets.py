from .models import Quote
from .serializers import QuoteSerializer

from rest_framework import viewsets


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer