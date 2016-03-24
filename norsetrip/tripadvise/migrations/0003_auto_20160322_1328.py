# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0002_auto_20160313_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodge',
            name='average_rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(db_column=b'Rating', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
    ]
