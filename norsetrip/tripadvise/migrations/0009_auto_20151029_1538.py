# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0008_auto_20151027_1702'),
    ]

    operations = [
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
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.EmailField(max_length=254, serialize=False, primary_key=True, db_column=b'UserId')),
                ('role', models.CharField(max_length=9, db_column=b'ROLE', choices=[(b'PROFESSOR', b'PROFESSOR'), (b'ALUMNI', b'STUDENT'), (b'FACULTY', b'FACULTY')])),
            ],
        ),
        migrations.RemoveField(
            model_name='lodge',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='review',
            name='lodge_Id',
            field=models.ForeignKey(to='tripadvise.Lodge', db_column=b'LodgeID FK'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column=b'UserId FK'),
        ),
        migrations.AddField(
            model_name='course_assignment',
            name='user_Id',
            field=models.ForeignKey(to='tripadvise.User', db_column=b'UserId FK'),
        ),
    ]
