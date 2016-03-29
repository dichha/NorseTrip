# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0015_auto_20160326_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=24, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullName',
            field=models.CharField(max_length=5, verbose_name=b'Full Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=9, verbose_name=b'Role', choices=[(b'PROFESSOR', b'PROFESSOR'), (b'STUDENT', b'STUDENT'), (b'ALUMNI', b'ALUMNI'), (b'FACULTY', b'FACULTY')]),
        ),
    ]
