# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0027_auto_20160421_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='author',
            field=models.EmailField(max_length=24, null=True, verbose_name=b'Author'),
        ),
        migrations.AddField(
            model_name='food',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'Date Published'),
        ),
        migrations.AddField(
            model_name='food',
            name='user_Id',
            field=models.ForeignKey(db_column=b'UserId FK', to='tripadvise.CustomUser', null=True),
        ),
    ]
