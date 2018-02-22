# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_items_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
