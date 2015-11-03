# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0002_auto_20151024_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year_offered',
            field=models.IntegerField(db_column=b'Year Offered'),
        ),
    ]
