# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-23 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roster', '0010_auto_20181008_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodycam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('video', models.CharField(max_length=1000)),
                ('description', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Description')),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.IntegerField(choices=[(0, 'AL'), (1, 'AK'), (2, 'AZ'), (3, 'AR'), (4, 'CA'), (5, 'CO'), (6, 'CT'), (7, 'DE'), (8, 'FL'), (9, 'GA'), (10, 'HI'), (11, 'ID'), (12, 'IL'), (13, 'IN'), (14, 'IA'), (15, 'KS'), (16, 'KY'), (17, 'LA'), (18, 'ME'), (19, 'MD'), (20, 'MA'), (21, 'MI'), (22, 'MN'), (23, 'MS'), (24, 'MO'), (25, 'MT'), (26, 'NE'), (27, 'NV'), (28, 'NH'), (29, 'NJ'), (30, 'NM'), (31, 'NY'), (32, 'NC'), (33, 'ND'), (34, 'OH'), (35, 'OK'), (36, 'OR'), (37, 'PA'), (38, 'RI'), (39, 'SC'), (40, 'SD'), (41, 'TN'), (42, 'TX'), (43, 'UT'), (44, 'VT'), (45, 'VA'), (46, 'WA'), (47, 'WV'), (48, 'WI'), (49, 'WY'), (50, 'DC'), (51, 'PR'), (52, 'GU')], verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=256, null=True, verbose_name='City')),
                ('shooting', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roster.Shooting')),
            ],
        ),
    ]
