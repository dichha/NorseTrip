# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0014_auto_20160326_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name=b'Comment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date Published'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(verbose_name=b'Rating', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewId',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
