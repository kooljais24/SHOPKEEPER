# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class items(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    pos=models.CharField(max_length=3)
    owner = models.ForeignKey( User, related_name='items', on_delete=models.CASCADE)
	

    class Meta:
        ordering = ('created',)
