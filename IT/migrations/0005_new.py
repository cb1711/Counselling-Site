# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0004_message_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=100)),
            ],
        ),
    ]
