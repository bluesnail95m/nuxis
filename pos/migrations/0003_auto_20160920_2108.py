# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='payment_type',
            new_name='payment_method',
        ),
    ]
