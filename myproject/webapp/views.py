# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from webapp.models import items
from webapp.serializers import itemsSerializer
# Create your views here.
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from webapp.serializers import UserSerializer
from rest_framework import permissions
from webapp.permissions import IsOwnerOrReadOnly
#Using format suffixes gives us URLs that explicitly refer to a given format
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import filters


class itemsList(generics.ListCreateAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly) #this lets the other users to have a look on others data but only in readable mode
    def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class itemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly) #for making lists visible to all need to use IsAuthenticatedOrReadOnly in permission_classes

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(CreateAPIView):
	model = get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer
