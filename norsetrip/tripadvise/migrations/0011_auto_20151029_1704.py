# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0010_auto_20151029_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=9, db_column=b'ROLE', choices=[(b'PROFESSOR', b'PROFESSOR'), (b'STUDENT', b'STUDENT'), (b'ALUMNI', b'ALUMNI'), (b'FACULTY', b'FACULTY')]),
        ),
    ]
