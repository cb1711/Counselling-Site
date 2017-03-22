# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellor',
            name='Type',
            field=models.CharField(choices=[('Emotional', 'Emotional'), ('Academic', 'Academic')], max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='Year',
            field=models.CharField(choices=[('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016')], max_length=4),
        ),
    ]
