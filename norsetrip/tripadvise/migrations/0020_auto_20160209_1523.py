# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0019_auto_20151207_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lodge_membership',
            field=models.ManyToManyField(to='tripadvise.Lodge', through='tripadvise.Membership'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='lodge',
            field=models.ForeignKey(to='tripadvise.Lodge'),
        ),
    ]
