# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tripadvise', '0013_auto_20160326_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year_offered',
            field=models.IntegerField(default=2016, verbose_name=b'Year Offered', choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)]),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='city',
            field=models.CharField(max_length=100, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name=b'Country'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodgeId',
            field=models.AutoField(serialize=False, verbose_name=b'LodgeId', primary_key=True),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_address',
            field=models.CharField(max_length=200, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_descrip',
            field=models.TextField(verbose_name=b'Lodge Description'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_image',
            field=models.ImageField(upload_to=b'', width_field=b'width_field', height_field=b'height_field', blank=True, null=True, verbose_name=b'Lodge Image'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='lodge',
            name='lodge_url',
            field=models.URLField(verbose_name=b'Lodge URL'),
        ),
    ]
