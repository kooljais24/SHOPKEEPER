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



#Using format suffixes gives us URLs that explicitly refer to a given format

class itemsList(generics.ListCreateAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer


class itemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializer