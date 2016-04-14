# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tripadvise', '0023_auto_20160413_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.EmailField(default='temp@temp.com', max_length=24, verbose_name=b'Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user_Id',
            field=models.ForeignKey(db_column=b'UserId FK', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
