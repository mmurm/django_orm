# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-15 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_author', '0003_auto_20190515_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='books',
            new_name='Book',
        ),
    ]