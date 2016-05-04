# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0034_auto_20160503_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainmentreview',
            name='entertainment_Id',
            field=models.ForeignKey(to='tripadvise.Entertainment'),
        ),
    ]
