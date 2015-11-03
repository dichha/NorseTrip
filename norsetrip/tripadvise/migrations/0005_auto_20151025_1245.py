# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0004_auto_20151025_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodge',
            name='average_rating',
            field=models.IntegerField(default=100, db_column=b'Average Rating'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='course_Id',
            field=models.ForeignKey(verbose_name=b'course stayed in the lodge', to='tripadvise.Course'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='lodge_Id',
            field=models.ForeignKey(verbose_name=b'lodge where course students stayed', to='tripadvise.Lodge'),
        ),
    ]
