# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-26 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bodycams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodycamTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Text')),
            ],
        ),
        migrations.AddField(
            model_name='bodycam',
            name='date',
            field=models.DateField(default=datetime.date(2018, 10, 26)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bodycamtag',
            name='shooting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='bodycams.Bodycam'),
        ),
    ]
