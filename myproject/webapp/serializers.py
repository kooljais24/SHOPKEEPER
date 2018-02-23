from rest_framework import serializers
from webapp.models import items
from django.contrib.auth.models import User



class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ('id', 'name', 'price', 'quantity', 'pos')




class UserSerializer(serializers.ModelSerializer):
    webapp = serializers.PrimaryKeyRelatedField(many=True, queryset=items.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ('id', 'username', 'webapp','owner',)