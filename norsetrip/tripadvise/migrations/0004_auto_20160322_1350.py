# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0003_auto_20160322_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_Id',
        ),
    ]
