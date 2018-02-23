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

from django.contrib.auth.models import User
from webapp.serializers import UserSerializer
from rest_framework import permissions
from webapp.permissions import IsOwnerOrReadOnly
#Using format suffixes gives us URLs that explicitly refer to a given format

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse




class itemsList(generics.ListCreateAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly) #this lets the other users to have a look on others data but only in readable mode
    def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class itemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


