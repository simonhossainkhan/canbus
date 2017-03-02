# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('rpm', models.CharField(max_length=100)),
                ('mph', models.CharField(max_length=100)),
                ('throttle', models.CharField(max_length=100)),
                ('load', models.CharField(max_length=100)),
                ('fuel_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_fuel', models.CharField(max_length=50)),
                ('end_fuel', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tripinformation',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Trips'),
        ),
    ]
