# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cleaner', '0003_auto_20170220_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='issues',
            field=models.IntegerField(default=0),
        ),
    ]
