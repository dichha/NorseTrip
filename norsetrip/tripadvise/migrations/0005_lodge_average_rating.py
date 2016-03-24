# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0004_auto_20160322_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodge',
            name='average_rating',
            field=models.IntegerField(default=100, db_column=b'Average Rating'),
        ),
    ]
