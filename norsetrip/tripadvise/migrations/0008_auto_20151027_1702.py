# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0007_auto_20151027_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.IntegerField(serialize=False, primary_key=True, db_column=b'CourseId'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='lodgeAssignId',
            field=models.AutoField(serialize=False, primary_key=True, db_column=b'LodgeAssignId'),
        ),
    ]
