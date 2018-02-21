from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import items
from .serializers import itemsSerializer

# Create your views here.

class itemlist(APIView):

	def get(self,request):
		items1=items.objects.all()
		serializer=itemsSerializer(items1,many=True)
		return Response(serializer.data)

	def post(self):
		pass

