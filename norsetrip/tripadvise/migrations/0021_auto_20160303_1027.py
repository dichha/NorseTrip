# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0020_auto_20160209_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Lodge_Assignment',
            fields=[
                ('clAssignId', models.AutoField(serialize=False, primary_key=True, db_column=b'CourseLodgeAssignId')),
            ],
        ),
        migrations.RemoveField(
            model_name='membership',
            name='course',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='lodge',
        ),
        migrations.AlterModelOptions(
            name='lodge',
            options={'ordering': ['-lodgeId']},
        ),
        migrations.RemoveField(
            model_name='course',
            name='lodge_membership',
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
        migrations.DeleteModel(
            name='Membership',
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
            field=models.ManyToManyField(to='tripadvise.Lodge', through='tripadvise.Course_Lodge_Assignment'),
        ),
    ]
