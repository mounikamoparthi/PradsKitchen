# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='Image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]