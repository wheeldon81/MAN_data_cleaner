# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cleaner', '0002_auto_20170219_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=6)),
                ('edition', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='plate_edition',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='plate',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='slug',
        ),
        migrations.AddField(
            model_name='plate',
            name='ship',
            field=models.ForeignKey(default=b'', to='Cleaner.Ship'),
        ),
        migrations.AddField(
            model_name='item',
            name='plate',
            field=models.ForeignKey(default=b'', to='Cleaner.Plate'),
        ),
    ]
