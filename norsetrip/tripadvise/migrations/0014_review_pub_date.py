# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0013_auto_20151103_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=None, db_column=b'Date'),
        ),
    ]
