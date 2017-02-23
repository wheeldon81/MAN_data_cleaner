# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cleaner', '0004_ship_issues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship',
            old_name='issues',
            new_name='issue',
        ),
    ]
