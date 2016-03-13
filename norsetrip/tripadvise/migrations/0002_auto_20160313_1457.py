# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course_user_assignments',
            field=models.ManyToManyField(to='tripadvise.Course', through='tripadvise.Course_User_Assignment'),
        ),
        migrations.AlterUniqueTogether(
            name='course_lodge_assignment',
            unique_together=set([('lodge_name', 'course_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='course_user_assignment',
            unique_together=set([('course_Id', 'user_Id')]),
        ),
        migrations.AlterUniqueTogether(
            name='lodge',
            unique_together=set([('lodge_name', 'lodge_address', 'city', 'country', 'lodge_url')]),
        ),
    ]
