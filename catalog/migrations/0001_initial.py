# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-25 22:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an auction name', max_length=200)),
                ('start_time', models.DateTimeField(help_text='Enter a starting time')),
                ('duration', models.DurationField(help_text='Enter a duration time')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a category of auction (e.g. Charity, Electronics etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a lot name', max_length=200)),
                ('start_price', models.DecimalField(decimal_places=3, help_text='Enter a starting price', max_digits=10)),
                ('start_time', models.DateTimeField(help_text='Enter a starting time')),
                ('duration', models.DurationField(help_text='Enter a duration time')),
                ('step', models.DecimalField(decimal_places=3, help_text='Enter a starting price', max_digits=10)),
                ('is_tender', models.BooleanField()),
                ('is_sold', models.BooleanField()),
                ('auction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Auction')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.ManyToManyField(help_text='Select a category for this auction', to='catalog.Category'),
        ),
    ]