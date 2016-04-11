# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0020_auto_20160409_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rqmt',
            field=multiselectfield.db.fields.MultiSelectField(default=b'INTCL', max_length=41, verbose_name=b'Requirement(s) Filled', choices=[(b'INTCL', b'INTERCULTURAL'), (b'HB', b'HUMAN BEHAVIOR'), (b'HBSSM', b'HUMAN EXPRESSION SOCIAL SCIENCE METHODS'), (b'HEPT', b'HUMAN EXPRESSION PRIMARY TEXT'), (b'HIST', b'HISTORICAL'), (b'JTERM II', b'SECOND JTERM'), (b'NOTTINGHAM', b'NOTTINGHAM'), (b'NWL', b'NATURAL WORLD LAB'), (b'NWNL', b'NATURAL WORLD NON LAB'), (b'QUANT', b'QUANTTITAVE'), (b'REL II', b'RELIGION II'), (b'ROCHESTER', b'ROCHESTER'), (b'PAID 450', b'PAIDIEA 450'), (b'WASHINGTON', b'WASHINGTON')]),
        ),
    ]
