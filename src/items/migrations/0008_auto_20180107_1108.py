# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_remove_item_returner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='claimer',
            field=models.CharField(blank=True, help_text='do not forget to put a claimer', max_length=120, null=True),
        ),
    ]
