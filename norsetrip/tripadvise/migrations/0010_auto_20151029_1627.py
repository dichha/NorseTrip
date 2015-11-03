# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0009_auto_20151029_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=16, db_column=b'Cost', choices=[(1, b'Very Cheap'), (2, b'Pretty Cheap'), (3, b'Average'), (4, b'Pretty Expensive'), (5, b'Very Expensive')]),
        ),
    ]
