# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0017_auto_20151207_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lodge_membership',
            field=models.ManyToManyField(related_name='_course_lodge_membership_+', through='tripadvise.Membership', to='tripadvise.Lodge'),
        ),
    ]
