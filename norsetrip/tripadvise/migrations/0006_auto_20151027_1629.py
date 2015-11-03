# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0005_auto_20151025_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='course_Id',
            field=models.ForeignKey(verbose_name=b'CourseId FK', to='tripadvise.Course'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='lodge_Id',
            field=models.ForeignKey(verbose_name=b'LodgeId FK', to='tripadvise.Lodge'),
        ),
    ]
