# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    replaces = [(b'tripadvise', '0001_initial'), (b'tripadvise', '0002_auto_20151024_2356'), (b'tripadvise', '0003_auto_20151025_0007'), (b'tripadvise', '0004_auto_20151025_1119'), (b'tripadvise', '0005_auto_20151025_1245'), (b'tripadvise', '0006_auto_20151027_1629'), (b'tripadvise', '0007_auto_20151027_1647'), (b'tripadvise', '0008_auto_20151027_1702'), (b'tripadvise', '0009_auto_20151029_1538'), (b'tripadvise', '0010_auto_20151029_1627'), (b'tripadvise', '0011_auto_20151029_1704'), (b'tripadvise', '0012_auto_20151029_1722'), (b'tripadvise', '0013_auto_20151103_1549'), (b'tripadvise', '0014_review_pub_date'), (b'tripadvise', '0015_auto_20151103_1656'), (b'tripadvise', '0016_auto_20151104_1134'), (b'tripadvise', '0017_auto_20151207_1924'), (b'tripadvise', '0018_auto_20151207_2142'), (b'tripadvise', '0019_auto_20151207_2145'), (b'tripadvise', '0020_auto_20160209_1523'), (b'tripadvise', '0021_auto_20160303_1027'), (b'tripadvise', '0022_auto_20160306_1126')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(serialize=False, primary_key=True, db_column=b'CourseId')),
                ('name', models.CharField(max_length=200, db_column=b'Name')),
                ('dept', models.CharField(max_length=200, db_column=b'Department')),
                ('prof', models.CharField(max_length=200, db_column=b'Professor')),
                ('year_offered', models.IntegerField(db_column=b'Year Offered')),
                ('term', models.CharField(default=b'JTERM', max_length=8, choices=[(b'JTERM', b'JTERM'), (b'SUMMER', b'SUMMER'), (b'YEAR', b'YEAR'), (b'SEMESTER', b'SEMESTER')])),
            ],
        ),
        migrations.CreateModel(
            name='Lodge',
            fields=[
                ('lodgeId', models.AutoField(serialize=False, primary_key=True, db_column='LodgeId')),
                ('lodge_name', models.CharField(max_length=200, db_column='Name')),
                ('lodge_address', models.CharField(max_length=200, db_column='Address')),
                ('city', models.CharField(max_length=100, db_column='City')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('lodge_url', models.URLField(db_column='URL')),
                ('lodge_descrip', models.TextField(db_column='Description')),
                ('average_rating', models.IntegerField(default=100, db_column='Average Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Assignment',
            fields=[
                ('courseAssignId', models.AutoField(serialize=False, primary_key=True, db_column=b'Course_AssignmentId')),
                ('course_Id', models.ForeignKey(to='tripadvise.Course', db_column=b'CourseId FK')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewId', models.AutoField(serialize=False, primary_key=True, db_column=b'ReviewId')),
                ('rating', models.IntegerField(db_column=b'Rating', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('cost', models.IntegerField(db_column=b'Cost', choices=[(1, b'Very Cheap'), (2, b'Pretty Cheap'), (3, b'Average'), (4, b'Pretty Expensive'), (5, b'Very Expensive')])),
                ('comment', models.TextField(db_column=b'Comment')),
                ('lodge_Id', models.ForeignKey(to='tripadvise.Lodge', db_column=b'LodgeID FK')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(serialize=False, primary_key=True, db_column='UserId')),
                ('role', models.CharField(max_length=9, db_column='ROLE', choices=[('PROFESSOR', 'PROFESSOR'), ('STUDENT', 'STUDENT'), ('ALUMNI', 'ALUMNI'), ('FACULTY', 'FACULTY')])),
                ('email', models.EmailField(max_length=24, db_column='Email')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column='UserId FK'),
        ),
        migrations.AddField(
            model_name='course_assignment',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column='UserId FK'),
        ),
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=16, db_column=b'Cost', choices=[(1, b'Very Cheap'), (2, b'Pretty Cheap'), (3, b'Average'), (4, b'Pretty Expensive'), (5, b'Very Expensive')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=16, db_column=b'Cost', choices=[(b'1', b'Very Cheap'), (b'2', b'Pretty Cheap'), (b'3', b'Average'), (b'4', b'Pretty Expensive'), (b'5', b'Very Expensive')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, db_column=b'Rating', choices=[(b'ONE', b'1'), (b'TWO', b'2'), (b'THREE', b'3'), (b'FOUR', b'4'), (b'FIVE', b'5')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(max_length=200, db_column=b'Department', choices=[(b'AFRICANA STUDIES', b'AFRICANA STUDIES'), (b'BIOLOGY', b'BIOLOGY'), (b'CHEMISTRY', b'CHEMISTRY'), (b'CLASSICS', b'CLASSICS'), (b'COMMUNICATION STUDIES', b'COMMUNICATION STUDIES'), (b'COMPUTER SCIENCE', b'COMPUTER SCIENCE'), (b'ECONOMICS AND BUSINESS', b'ECONOMICS AND BUSINESS'), (b'EDUCATION', b'EDUCATION'), (b'ENGLISH', b'ENGLISH'), (b'ENVIRONMENTAL STUDIES', b'ENVIRONMENTAL STUDIES'), (b'HEALTH AND PHYSICAL EDUCATION', b'HEALTH AND PHYSICAL EDUCATION'), (b'HISTORY', b'HISTORY'), (b'INTERNATIONAL STUDIES', b'INTERNATIONAL STUDIES'), (b'LIBRARY AND INFORMATION STUDIES', b'LIBRARY AND INFORMATION STUDIES'), (b'MATHEMATICS', b'MATHEMATICS'), (b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS', b'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), (b'MUSEUM STUDIES', b'MUSEUM STUDIES'), (b'MUSIC', b'MUSIC'), (b'NURSING', b'NURSING'), (b'PAIDIEA', b'PAIDIEA'), (b'PHILOSOPHY', b'PHILOSOPHY'), (b'PHYSICS', b'PHYSICS'), (b'POLITICAL SCIENCE', b'POLITICAL SCIENCE'), (b'PSYCHOLOGY', b'PSYCHOLOGY'), (b'RELIGION', b'RELIGION'), (b'RUSSIAN STUDIES', b'RUSSIAN STUDIES'), (b'SCHOLARS PROGRAM', b'SCHOLARS PROGRAM'), (b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', b'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), (b'VISUAL AND PERFORMING ARTS', b'VISUAL AND PERFORMING ARTS'), (b'WOMEN AND GENDER STUDIES', b'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, db_column=b'Rating', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(db_column='Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='CourseId'),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(max_length=200, db_column='Department', choices=[('AFRICANA STUDIES', 'AFRICANA STUDIES'), ('BIOLOGY', 'BIOLOGY'), ('CHEMISTRY', 'CHEMISTRY'), ('CLASSICS', 'CLASSICS'), ('COMMUNICATION STUDIES', 'COMMUNICATION STUDIES'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('ECONOMICS AND BUSINESS', 'ECONOMICS AND BUSINESS'), ('EDUCATION', 'EDUCATION'), ('ENGLISH', 'ENGLISH'), ('ENVIRONMENTAL STUDIES', 'ENVIRONMENTAL STUDIES'), ('HEALTH AND PHYSICAL EDUCATION', 'HEALTH AND PHYSICAL EDUCATION'), ('HISTORY', 'HISTORY'), ('INTERNATIONAL STUDIES', 'INTERNATIONAL STUDIES'), ('LIBRARY AND INFORMATION STUDIES', 'LIBRARY AND INFORMATION STUDIES'), ('MATHEMATICS', 'MATHEMATICS'), ('MODERN LANGUAGES, LITERATURES AND LINGUISTICS', 'MODERN LANGUAGES, LITERATURES AND LINGUISTICS'), ('MUSEUM STUDIES', 'MUSEUM STUDIES'), ('MUSIC', 'MUSIC'), ('NURSING', 'NURSING'), ('PAIDIEA', 'PAIDIEA'), ('PHILOSOPHY', 'PHILOSOPHY'), ('PHYSICS', 'PHYSICS'), ('POLITICAL SCIENCE', 'POLITICAL SCIENCE'), ('PSYCHOLOGY', 'PSYCHOLOGY'), ('RELIGION', 'RELIGION'), ('RUSSIAN STUDIES', 'RUSSIAN STUDIES'), ('SCHOLARS PROGRAM', 'SCHOLARS PROGRAM'), ('SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', 'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'), ('VISUAL AND PERFORMING ARTS', 'VISUAL AND PERFORMING ARTS'), ('WOMEN AND GENDER STUDIES', 'WOMEN AND GENDER STUDIES')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, db_column='Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof',
            field=models.CharField(max_length=200, db_column='Professor'),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.CharField(default='JTERM', max_length=8, choices=[('JTERM', 'JTERM'), ('SUMMER', 'SUMMER'), ('YEAR', 'YEAR'), ('SEMESTER', 'SEMESTER')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='year_offered',
            field=models.IntegerField(db_column='Year Offered'),
        ),
        migrations.AlterField(
            model_name='course_assignment',
            name='courseAssignId',
            field=models.AutoField(serialize=False, primary_key=True, db_column='Course_AssignmentId'),
        ),
        migrations.AlterField(
            model_name='course_assignment',
            name='course_Id',
            field=models.ForeignKey(to='tripadvise.Course', db_column='CourseId FK'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(db_column='Comment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='cost',
            field=models.CharField(max_length=16, db_column='Cost', choices=[('1', 'Very Cheap'), ('2', 'Pretty Cheap'), ('3', 'Average'), ('4', 'Pretty Expensive'), ('5', 'Very Expensive')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='lodge_Id',
            field=models.ForeignKey(to='tripadvise.Lodge', db_column='LodgeID FK'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, db_column='Rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewId',
            field=models.AutoField(serialize=False, primary_key=True, db_column='ReviewId'),
        ),
        migrations.CreateModel(
            name='Course_Lodge_Assignment',
            fields=[
                ('clAssignId', models.AutoField(serialize=False, primary_key=True, db_column=b'CourseLodgeAssignId')),
            ],
        ),
        migrations.AlterModelOptions(
            name='lodge',
            options={'ordering': ['-lodgeId']},
        ),
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(null=True, db_column=b'Desciption'),
        ),
        migrations.AddField(
            model_name='lodge',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lodge',
            name='lodge_image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='lodge',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course_lodge_assignment',
            name='course_name',
            field=models.ForeignKey(to='tripadvise.Course'),
        ),
        migrations.AddField(
            model_name='course_lodge_assignment',
            name='lodge_name',
            field=models.ForeignKey(to='tripadvise.Lodge'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_lodge_assignments',
            field=models.ManyToManyField(to=b'tripadvise.Lodge', through='tripadvise.Course_Lodge_Assignment'),
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-courseId']},
        ),
    ]
