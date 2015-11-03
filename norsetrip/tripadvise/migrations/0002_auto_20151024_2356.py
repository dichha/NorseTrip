# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(serialize=False, primary_key=True, db_column=b'CourseId')),
                ('name', models.CharField(max_length=200, db_column=b'Name')),
                ('dept', models.CharField(max_length=200, db_column=b'Department')),
                ('prof', models.CharField(max_length=200, db_column=b'Professor')),
                ('year_offered', models.IntegerField(max_length=4, db_column=b'Year Offered')),
                ('term', models.CharField(default=b'JTERM', max_length=8, choices=[(b'JTERM', b'JTERM'), (b'SUMMER', b'SUMMER'), (b'YEAR', b'YEAR'), (b'SEMESTER', b'SEMESTER')])),
            ],
        ),
        migrations.CreateModel(
            name='Course_Lodge_Assignment',
            fields=[
                ('lodgeAssignId', models.IntegerField(serialize=False, primary_key=True, db_column=b'LodgeAssignId')),
                ('course_Id', models.ForeignKey(verbose_name=b'courseId', to='tripadvise.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lodge',
            fields=[
                ('lodgeId', models.IntegerField(serialize=False, primary_key=True, db_column=b'LodgeId')),
                ('lodge_name', models.CharField(max_length=200, db_column=b'Name')),
                ('lodge_address', models.CharField(max_length=200, db_column=b'Address')),
                ('city', models.CharField(max_length=100, db_column=b'City')),
                ('country', models.CharField(max_length=100, db_column=b'Country')),
                ('pub_date', models.DateTimeField(db_column=b'Date')),
                ('lodge_url', models.URLField(db_column=b'URL')),
                ('lodge_descrip', models.TextField(db_column=b'Description')),
                ('course_Id', models.ForeignKey(verbose_name=b'courseId', to='tripadvise.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='Lodging',
        ),
        migrations.AddField(
            model_name='course_lodge_assignment',
            name='lodge_Id',
            field=models.ForeignKey(verbose_name=b'lodgeId', to='tripadvise.Lodge'),
        ),
        migrations.AddField(
            model_name='course',
            name='lodge_Id',
            field=models.ForeignKey(verbose_name=b'lodgeId', to='tripadvise.Lodge'),
        ),
    ]
