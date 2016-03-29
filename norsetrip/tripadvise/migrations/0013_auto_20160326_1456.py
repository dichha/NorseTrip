# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0012_auto_20160326_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.IntegerField(serialize=False, verbose_name=b'Course Id', primary_key=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Course Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.CharField(default=b'JTERM', max_length=8, verbose_name=b'Term Offered', choices=[(b'JTERM', b'JTERM'), (b'SUMMER', b'SUMMER'), (b'YEAR', b'YEAR'), (b'SEMESTER', b'SEMESTER')]),
        ),
    ]
