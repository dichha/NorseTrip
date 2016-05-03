# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0031_auto_20160501_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(height_field=b'height_field', upload_to=b'', width_field=b'width_field', null=True, verbose_name=b'Food Image'),
        ),
    ]
