# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cleaner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='slug',
            field=models.CharField(default=b'plate_edition', max_length=10),
        ),
    ]
