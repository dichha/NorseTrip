# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0012_auto_20151029_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254, primary_key=True, db_column=b'Email'),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(max_length=200, db_column=b'Department', choices=[(b'AFRICANA STUDIES', b'AFRICANA STUDIES'), (b'BIOLOGY', b'BIOLOGY'), (b'CHEMISTRY', b'CHEMISTRY'), (b'CLASSICS', b'CLASSICS'), (b'COMMUNICATION STUDIES', b'COMMUNICATION STUDIES'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'ECONOMICS AND BUSINESS', b'ECONOMICS AND BUSINESS'), (b'EDUCATION', b'EDUCATION'), (b'ENGLISH', b'ENGLISH'), (b'ENVIRONMENTAL STUDIES', b'ENVIRONMENTAL STUDIES'), (b'HEALTH AND PHYSICAL EDUCATION', b'HEALTH AND PHYSICAL EDUCATION'), (b'HISTORY', b'HISTORY'), (b'INTERNATIONAL STUDIES', b'INTERNATIONAL STUDIES'), (b'LIBRARY AND INFORMATION STUDIES', b'LIBRARY AND INFORMATION STUDIES'), (b'MATHEMATICS', b'MATHEMATICS'), (b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS', b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), (b'MUSEUM STUDIES', b'MUSEUM STUDIES'), (b'MUSIC', b'MUSIC'), (b'NURSING', b'NURSING'), (b'PAIDIEA', b'PAIDIEA'), (b'PHILOSOPHY', b'PHILOSOPHY'), (b'PHYSICS', b'PHYSICS'), (b'POLITICAL SCIENCE', b'POLITICAL SCIENCE'), (b'PSYCHOLOGY', b'PSYCHOLOGY'), (b'RELIGION', b'RELIGION'), (b'RUSSIAN STUDIES', b'RUSSIAN STUDIES'), (b'SCHOLARS PROGRAM', b'SCHOLARS PROGRAM'), (b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), (b'VISUAL AND PERFORMING ARTS', b'VISUAL AND PERFORMING ARTS'), (b'WOMEN AND GENDER STUDIES', b'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, db_column=b'Rating', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.AutoField(serialize=False, primary_key=True, db_column=b'UserId'),
        ),
    ]
