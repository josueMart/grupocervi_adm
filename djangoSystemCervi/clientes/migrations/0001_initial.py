# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('direction', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('contactName', models.CharField(max_length=255)),
                ('telephoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('deliveryAddres', models.CharField(max_length=255)),
                ('rfc', models.CharField(max_length=255)),
                ('fiscalAddres', models.CharField(max_length=255)),
                ('salesPerson', models.CharField(max_length=255)),
                ('observations', models.TextField(max_length=400)),
            ],
        ),
    ]
