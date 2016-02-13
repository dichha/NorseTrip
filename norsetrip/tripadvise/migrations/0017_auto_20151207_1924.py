# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0016_auto_20151104_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_that_was_switched', models.CharField(max_length=65, db_column=b'Hotel that was Switched')),
                ('date_switched', models.DateField()),
                ('course', models.ForeignKey(to='tripadvise.Course')),
                ('lodge', models.ForeignKey(to='tripadvise.Lodge')),
            ],
        ),
        migrations.RemoveField(
            model_name='course_lodge_assignment',
            name='course_Id',
        ),
        migrations.RemoveField(
            model_name='course_lodge_assignment',
            name='lodge_Id',
        ),
        migrations.DeleteModel(
            name='Course_Lodge_Assignment',
        ),
        migrations.AddField(
            model_name='course',
            name='lodge_membership',
            field=models.ManyToManyField(to='tripadvise.Lodge', through='tripadvise.Membership'),
        ),
    ]
