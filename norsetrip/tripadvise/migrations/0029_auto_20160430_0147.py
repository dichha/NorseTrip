# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0028_auto_20160429_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to=b'', width_field=b'width_field', height_field=b'height_field', blank=True, null=True, verbose_name=b'Lodge Image'),
        ),
    ]
