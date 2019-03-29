# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roster', '0020_shooting_specially_exempted_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='shooting',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shootings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shooting',
            name='specially_exempted_users',
            field=models.ManyToManyField(related_name='exempted_shootings', to=settings.AUTH_USER_MODEL),
        ),
    ]
