# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0005_lodge_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='lodge_Id',
            field=models.ForeignKey(to='tripadvise.Lodge'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, db_column=b'Date', blank=True),
        ),
    ]
