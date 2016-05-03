# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0032_auto_20160502_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lodge',
            name='lodge_image',
            field=models.ImageField(height_field=b'height_field', upload_to=b'', width_field=b'width_field', null=True, verbose_name=b'Lodge Image'),
        ),
    ]
