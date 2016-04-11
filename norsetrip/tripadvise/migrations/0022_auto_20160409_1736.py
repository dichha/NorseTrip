# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0021_auto_20160409_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['fullName']},
        ),
        migrations.AlterField(
            model_name='user',
            name='fullName',
            field=models.CharField(max_length=50, verbose_name=b'Full Name'),
        ),
    ]
