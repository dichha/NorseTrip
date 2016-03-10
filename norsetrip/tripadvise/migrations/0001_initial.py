# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(serialize=False, primary_key=True, db_column=b'CourseId')),
                ('name', models.CharField(max_length=200, db_column=b'Name')),
                ('dept', models.CharField(max_length=200, db_column=b'Department', choices=[(b'AFRICANA STUDIES', b'AFRICANA STUDIES'), (b'BIOLOGY', b'BIOLOGY'), (b'CHEMISTRY', b'CHEMISTRY'), (b'CLASSICS', b'CLASSICS'), (b'COMMUNICATION STUDIES', b'COMMUNICATION STUDIES'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'ECONOMICS AND BUSINESS', b'ECONOMICS AND BUSINESS'), (b'EDUCATION', b'EDUCATION'), (b'ENGLISH', b'ENGLISH'), (b'ENVIRONMENTAL STUDIES', b'ENVIRONMENTAL STUDIES'), (b'HEALTH AND PHYSICAL EDUCATION', b'HEALTH AND PHYSICAL EDUCATION'), (b'HISTORY', b'HISTORY'), (b'INTERNATIONAL STUDIES', b'INTERNATIONAL STUDIES'), (b'LIBRARY AND INFORMATION STUDIES', b'LIBRARY AND INFORMATION STUDIES'), (b'MATHEMATICS', b'MATHEMATICS'), (b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS', b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), (b'MUSEUM STUDIES', b'MUSEUM STUDIES'), (b'MUSIC', b'MUSIC'), (b'NURSING', b'NURSING'), (b'PAIDIEA', b'PAIDIEA'), (b'PHILOSOPHY', b'PHILOSOPHY'), (b'PHYSICS', b'PHYSICS'), (b'POLITICAL SCIENCE', b'POLITICAL SCIENCE'), (b'PSYCHOLOGY', b'PSYCHOLOGY'), (b'RELIGION', b'RELIGION'), (b'RUSSIAN STUDIES', b'RUSSIAN STUDIES'), (b'SCHOLARS PROGRAM', b'SCHOLARS PROGRAM'), (b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), (b'VISUAL AND PERFORMING ARTS', b'VISUAL AND PERFORMING ARTS'), (b'WOMEN AND GENDER STUDIES', b'WOMEN AND GENDER STUDIES')])),
                ('prof', models.CharField(max_length=200, db_column=b'Professor')),
                ('year_offered', models.IntegerField(db_column=b'Year Offered')),
                ('term', models.CharField(default=b'JTERM', max_length=8, choices=[(b'JTERM', b'JTERM'), (b'SUMMER', b'SUMMER'), (b'YEAR', b'YEAR'), (b'SEMESTER', b'SEMESTER')])),
                ('course_description', models.TextField(null=True, db_column=b'Desciption')),
            ],
            options={
                'ordering': ['-courseId'],
            },
        ),
        migrations.CreateModel(
            name='Course_Lodge_Assignment',
            fields=[
                ('clAssignId', models.AutoField(serialize=False, primary_key=True, db_column=b'CourseLodgeAssignId')),
                ('course_name', models.ForeignKey(to='tripadvise.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_User_Assignment',
            fields=[
                ('courseAssignId', models.AutoField(serialize=False, primary_key=True, db_column=b'Course_AssignmentId')),
                ('course_Id', models.ForeignKey(to='tripadvise.Course', db_column=b'CourseId FK')),
            ],
        ),
        migrations.CreateModel(
            name='Lodge',
            fields=[
                ('lodgeId', models.AutoField(serialize=False, primary_key=True, db_column=b'LodgeId')),
                ('lodge_name', models.CharField(max_length=200, db_column=b'Name')),
                ('lodge_address', models.CharField(max_length=200, db_column=b'Address')),
                ('city', models.CharField(max_length=100, db_column=b'City')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('lodge_url', models.URLField(db_column=b'URL')),
                ('lodge_descrip', models.TextField(db_column=b'Description')),
                ('average_rating', models.IntegerField(default=100, db_column=b'Average Rating')),
                ('lodge_image', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'', blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-lodgeId'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewId', models.AutoField(serialize=False, primary_key=True, db_column=b'ReviewId')),
                ('rating', models.CharField(max_length=1, db_column=b'Rating', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('cost', models.CharField(max_length=16, db_column=b'Cost', choices=[(b'1', b'Very Cheap'), (b'2', b'Pretty Cheap'), (b'3', b'Average'), (b'4', b'Pretty Expensive'), (b'5', b'Very Expensive')])),
                ('comment', models.TextField(db_column=b'Comment')),
                ('pub_date', models.DateTimeField(db_column=b'Date')),
                ('lodge_Id', models.ForeignKey(to='tripadvise.Lodge', db_column=b'LodgeID FK')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(serialize=False, primary_key=True, db_column=b'UserId')),
                ('fullName', models.CharField(max_length=50, db_column=b'Name')),
                ('email', models.EmailField(max_length=24, db_column=b'Email')),
                ('role', models.CharField(max_length=9, db_column=b'ROLE', choices=[(b'PROFESSOR', b'PROFESSOR'), (b'STUDENT', b'STUDENT'), (b'ALUMNI', b'ALUMNI'), (b'FACULTY', b'FACULTY')])),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column=b'UserId FK'),
        ),
        migrations.AddField(
            model_name='course_user_assignment',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column=b'UserId FK'),
        ),
        migrations.AddField(
            model_name='course_lodge_assignment',
            name='lodge_name',
            field=models.ForeignKey(to='tripadvise.Lodge'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_lodge_assignments',
            field=models.ManyToManyField(to='tripadvise.Lodge', through='tripadvise.Course_Lodge_Assignment'),
        ),
    ]
