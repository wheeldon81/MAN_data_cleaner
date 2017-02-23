# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.IntegerField(default=0)),
                ('order_number', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=5)),
                ('plate', models.CharField(max_length=6)),
                ('edition', models.CharField(max_length=3)),
                ('slug', models.CharField(default=b'plate_edition', unique=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='plate_edition',
            field=models.ForeignKey(to='Cleaner.Ship'),
        ),
    ]
