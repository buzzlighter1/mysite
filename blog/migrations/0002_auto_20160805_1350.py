# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='new user', max_length=140),
        ),
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.FileField(default='settings.MEDIA_ROOT/media/default.png', upload_to=''),
        ),
    ]