# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0030_auto_20160430_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(default=b'STUDENT', max_length=9, verbose_name=b'Role', choices=[(b'STUDENT', b'STUDENT'), (b'PROFESSOR', b'PROFESSOR'), (b'ALUMNI', b'ALUMNI'), (b'FACULTY', b'FACULTY')]),
        ),
    ]
