# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0033_auto_20160502_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('entertainmentId', models.AutoField(serialize=False, primary_key=True, db_column=b'EntertainmentId')),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('author', models.EmailField(max_length=24, null=True, verbose_name=b'Author')),
                ('address', models.CharField(max_length=200, verbose_name=b'Address')),
                ('city', models.CharField(max_length=100, verbose_name=b'City')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name=b'Country')),
                ('url', models.URLField(null=True, verbose_name=b'URL', blank=True)),
                ('descrip', models.TextField(verbose_name=b'Entertainment Description')),
                ('pub_date', models.DateTimeField(null=True, verbose_name=b'Date Published')),
                ('image', models.ImageField(height_field=b'height_field', upload_to=b'', width_field=b'width_field', null=True, verbose_name=b'Entertainment Image')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('user_Id', models.ForeignKey(db_column=b'UserId FK', to='tripadvise.CustomUser', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EntertainmentReview',
            fields=[
                ('reviewId', models.AutoField(serialize=False, primary_key=True)),
                ('author', models.EmailField(max_length=24, verbose_name=b'Author')),
                ('rating', models.IntegerField(verbose_name=b'Rating', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('comment', models.TextField(verbose_name=b'Comment')),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('likes', models.IntegerField(default=0)),
                ('entertainment_Id', models.ForeignKey(to='tripadvise.Food')),
                ('user_Id', models.ForeignKey(to='tripadvise.CustomUser', db_column=b'UserId FK')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='entertainment',
            unique_together=set([('name', 'address', 'city', 'country', 'url')]),
        ),
    ]
