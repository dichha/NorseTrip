# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0018_auto_20151207_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='lodge',
            field=models.ForeignKey(related_name='name', to='tripadvise.Lodge'),
        ),
    ]
