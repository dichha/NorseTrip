# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0011_auto_20151029_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=16, db_column=b'Cost', choices=[(b'1', b'Very Cheap'), (b'2', b'Pretty Cheap'), (b'3', b'Average'), (b'4', b'Pretty Expensive'), (b'5', b'Very Expensive')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, db_column=b'Rating', choices=[(b'ONE', b'1'), (b'TWO', b'2'), (b'THREE', b'3'), (b'FOUR', b'4'), (b'FIVE', b'5')]),
        ),
    ]
