# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plato', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('producto', models.ManyToManyField(blank=True, to='Producto.Producto')),
            ],
        ),
    ]