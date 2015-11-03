# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0003_auto_20151025_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lodge_Id',
        ),
        migrations.RemoveField(
            model_name='lodge',
            name='course_Id',
        ),
    ]
