# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0035_auto_20160503_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(max_length=200, verbose_name=b'Department', choices=[(b'AFRICANA STUDIES', b'AFRICANA STUDIES'), (b'BIOLOGY', b'BIOLOGY'), (b'CHEMISTRY', b'CHEMISTRY'), (b'CLASSICS', b'CLASSICS'), (b'COMMUNICATION STUDIES', b'COMMUNICATION STUDIES'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'ECONOMICS AND BUSINESS', b'ECONOMICS AND BUSINESS'), (b'EDUCATION', b'EDUCATION'), (b'ENGLISH', b'ENGLISH'), (b'ENVIRONMENTAL STUDIES', b'ENVIRONMENTAL STUDIES'), (b'HEALTH AND PHYSICAL EDUCATION', b'HEALTH AND PHYSICAL EDUCATION'), (b'HISTORY', b'HISTORY'), (b'INTERNATIONAL STUDIES', b'INTERNATIONAL STUDIES'), (b'LIBRARY AND INFORMATION STUDIES', b'LIBRARY AND INFORMATION STUDIES'), (b'MATHEMATICS', b'MATHEMATICS'), (b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS', b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), (b'MUSEUM STUDIES', b'MUSEUM STUDIES'), (b'MUSIC', b'MUSIC'), (b'NURSING', b'NURSING'), (b'PAIDEIA', b'PAIDEIA'), (b'PHILOSOPHY', b'PHILOSOPHY'), (b'PHYSICS', b'PHYSICS'), (b'POLITICAL SCIENCE', b'POLITICAL SCIENCE'), (b'PSYCHOLOGY', b'PSYCHOLOGY'), (b'RELIGION', b'RELIGION'), (b'RUSSIAN STUDIES', b'RUSSIAN STUDIES'), (b'SCHOLARS PROGRAM', b'SCHOLARS PROGRAM'), (b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), (b'VISUAL AND PERFORMING ARTS', b'VISUAL AND PERFORMING ARTS'), (b'WOMEN AND GENDER STUDIES', b'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='rqmt',
            field=multiselectfield.db.fields.MultiSelectField(default=b'INTCL', max_length=41, verbose_name=b'Requirement(s) Filled', choices=[(b'INTCL', b'INTERCULTURAL'), (b'HB', b'HUMAN BEHAVIOR'), (b'HBSSM', b'HUMAN EXPRESSION SOCIAL SCIENCE METHODS'), (b'HEPT', b'HUMAN EXPRESSION PRIMARY TEXT'), (b'HIST', b'HISTORICAL'), (b'JTERM II', b'SECOND JTERM'), (b'NOTTINGHAM', b'NOTTINGHAM'), (b'NWL', b'NATURAL WORLD LAB'), (b'NWNL', b'NATURAL WORLD NON LAB'), (b'QUANT', b'QUANTITAVE'), (b'REL II', b'RELIGION II'), (b'ROCHESTER', b'ROCHESTER'), (b'PAID 450', b'PAIDEIA 450'), (b'WASHINGTON', b'WASHINGTON')]),
        ),
    ]
