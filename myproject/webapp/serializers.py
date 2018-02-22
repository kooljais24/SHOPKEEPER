from rest_framework import serializers
from webapp.models import items


class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ('id', 'name', 'price', 'quantity', 'pos')