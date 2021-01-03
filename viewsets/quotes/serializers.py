from rest_framework import serializers

from quotes.models import Quote


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ('title', 'body', 'created')