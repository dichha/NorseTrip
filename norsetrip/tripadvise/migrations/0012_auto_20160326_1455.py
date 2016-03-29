# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0011_auto_20160326_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.IntegerField(serialize=False, verbose_name=b'Course Id', primary_key=True, db_column=b'CourseId'),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(max_length=200, verbose_name=b'Department', choices=[(b'AFRICANA STUDIES', b'AFRICANA STUDIES'), (b'BIOLOGY', b'BIOLOGY'), (b'CHEMISTRY', b'CHEMISTRY'), (b'CLASSICS', b'CLASSICS'), (b'COMMUNICATION STUDIES', b'COMMUNICATION STUDIES'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'ECONOMICS AND BUSINESS', b'ECONOMICS AND BUSINESS'), (b'EDUCATION', b'EDUCATION'), (b'ENGLISH', b'ENGLISH'), (b'ENVIRONMENTAL STUDIES', b'ENVIRONMENTAL STUDIES'), (b'HEALTH AND PHYSICAL EDUCATION', b'HEALTH AND PHYSICAL EDUCATION'), (b'HISTORY', b'HISTORY'), (b'INTERNATIONAL STUDIES', b'INTERNATIONAL STUDIES'), (b'LIBRARY AND INFORMATION STUDIES', b'LIBRARY AND INFORMATION STUDIES'), (b'MATHEMATICS', b'MATHEMATICS'), (b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS', b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), (b'MUSEUM STUDIES', b'MUSEUM STUDIES'), (b'MUSIC', b'MUSIC'), (b'NURSING', b'NURSING'), (b'PAIDIEA', b'PAIDIEA'), (b'PHILOSOPHY', b'PHILOSOPHY'), (b'PHYSICS', b'PHYSICS'), (b'POLITICAL SCIENCE', b'POLITICAL SCIENCE'), (b'PSYCHOLOGY', b'PSYCHOLOGY'), (b'RELIGION', b'RELIGION'), (b'RUSSIAN STUDIES', b'RUSSIAN STUDIES'), (b'SCHOLARS PROGRAM', b'SCHOLARS PROGRAM'), (b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), (b'VISUAL AND PERFORMING ARTS', b'VISUAL AND PERFORMING ARTS'), (b'WOMEN AND GENDER STUDIES', b'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Course Name', db_column=b'Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof',
            field=models.CharField(max_length=200, verbose_name=b'Professor'),
        ),
    ]
