from rest_framework import serializers
from webapp.models import items
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ('id', 'name', 'price', 'quantity', 'pos')




class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	#webapp = serializers.PrimaryKeyRelatedField(many=True, queryset=items.objects.all())
	#owner = serializers.ReadOnlyField(source='owner.username')
	def create(self,validated_data):
		user = get_user_model().objects.create(
		username = validated_data['username']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('username','password')	

