# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0015_auto_20151103_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.IntegerField(db_column='CourseId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(db_column='Department', max_length=200, choices=[('AFRICANA STUDIES', 'AFRICANA STUDIES'), ('BIOLOGY', 'BIOLOGY'), ('CHEMISTRY', 'CHEMISTRY'), ('CLASSICS', 'CLASSICS'), ('COMMUNICATION STUDIES', 'COMMUNICATION STUDIES'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('ECONOMICS AND BUSINESS', 'ECONOMICS AND BUSINESS'), ('EDUCATION', 'EDUCATION'), ('ENGLISH', 'ENGLISH'), ('ENVIRONMENTAL STUDIES', 'ENVIRONMENTAL STUDIES'), ('HEALTH AND PHYSICAL EDUCATION', 'HEALTH AND PHYSICAL EDUCATION'), ('HISTORY', 'HISTORY'), ('INTERNATIONAL STUDIES', 'INTERNATIONAL STUDIES'), ('LIBRARY AND INFORMATION STUDIES', 'LIBRARY AND INFORMATION STUDIES'), ('MATHEMATICS', 'MATHEMATICS'), ('MODERN LANGUAGES, LITERATURES AND LINGUISTICS', 'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), ('MUSEUM STUDIES', 'MUSEUM STUDIES'), ('MUSIC', 'MUSIC'), ('NURSING', 'NURSING'), ('PAIDIEA', 'PAIDIEA'), ('PHILOSOPHY', 'PHILOSOPHY'), ('PHYSICS', 'PHYSICS'), ('POLITICAL SCIENCE', 'POLITICAL SCIENCE'), ('PSYCHOLOGY', 'PSYCHOLOGY'), ('RELIGION', 'RELIGION'), ('RUSSIAN STUDIES', 'RUSSIAN STUDIES'), ('SCHOLARS PROGRAM', 'SCHOLARS PROGRAM'), ('SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', 'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), ('VISUAL AND PERFORMING ARTS', 'VISUAL AND PERFORMING ARTS'), ('WOMEN AND GENDER STUDIES', 'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(db_column='Name', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof',
            field=models.CharField(db_column='Professor', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.CharField(choices=[('JTERM', 'JTERM'), ('SUMMER', 'SUMMER'), ('YEAR', 'YEAR'), ('SEMESTER', 'SEMESTER')], max_length=8, default='JTERM'),
        ),
        migrations.AlterField(
            model_name='course',
            name='year_offered',
            field=models.IntegerField(db_column='Year Offered'),
        ),
        migrations.AlterField(
            model_name='course_assignment',
            name='courseAssignId',
            field=models.AutoField(db_column='Course_AssignmentId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_assignment',
            name='course_Id',
            field=models.ForeignKey(db_column='CourseId FK', to='tripadvise.Course'),
        ),
        migrations.AlterField(
            model_name='course_assignment',
            name='user_Id',
            field=models.ForeignKey(db_column='UserId FK', to='tripadvise.User'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='course_Id',
            field=models.ForeignKey(to='tripadvise.Course', verbose_name='CourseId FK'),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='lodgeAssignId',
            field=models.AutoField(db_column='LodgeAssignId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_lodge_assignment',
            name='lodge_Id',
            field=models.ForeignKey(to='tripadvise.Lodge', verbose_name='LodgeId FK'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='average_rating',
            field=models.IntegerField(db_column='Average Rating', default=100),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='city',
            field=models.CharField(db_column='City', max_length=100),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodgeId',
            field=models.AutoField(db_column='LodgeId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_address',
            field=models.CharField(db_column='Address', max_length=200),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_descrip',
            field=models.TextField(db_column='Description'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_name',
            field=models.CharField(db_column='Name', max_length=200),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_url',
            field=models.URLField(db_column='URL'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(db_column='Comment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(db_column='Cost', max_length=16, choices=[('1', 'Very Cheap'), ('2', 'Pretty Cheap'), ('3', 'Average'), ('4', 'Pretty Expensive'), ('5', 'Very Expensive')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='lodge_Id',
            field=models.ForeignKey(db_column='LodgeID FK', to='tripadvise.Lodge'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(db_column='Date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(db_column='Rating', max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewId',
            field=models.AutoField(db_column='ReviewId', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_Id',
            field=models.ForeignKey(db_column='UserId FK', to='tripadvise.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_column='Email', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(db_column='ROLE', max_length=9, choices=[('PROFESSOR', 'PROFESSOR'), ('STUDENT', 'STUDENT'), ('ALUMNI', 'ALUMNI'), ('FACULTY', 'FACULTY')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.AutoField(db_column='UserId', primary_key=True, serialize=False),
        ),
    ]
