# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0017_review_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rqmt',
            field=models.CharField(default=b'INTERCULTURAL', max_length=41, verbose_name=b'Requirement(s) Filled'),
        ),
    ]
