# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lodging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lodge_name', models.CharField(max_length=200, db_column=b'Name')),
                ('lodge_address', models.CharField(max_length=200, db_column=b'Address')),
                ('city', models.CharField(max_length=100, db_column=b'City')),
                ('country', models.CharField(max_length=100, db_column=b'Country')),
                ('pub_date', models.DateTimeField(db_column=b'Date')),
            ],
        ),
    ]
