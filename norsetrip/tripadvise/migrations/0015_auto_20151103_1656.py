# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0014_review_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(db_column=b'Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=24, db_column=b'Email'),
        ),
    ]
