# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_desa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dusun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_dusun', models.CharField(max_length=20)),
                ('nama_desa', models.ForeignKey(to='wilayah.Desa')),
            ],
        ),
        migrations.CreateModel(
            name='Kampung',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_kampung', models.CharField(max_length=20)),
                ('nama_dusun', models.ForeignKey(to='wilayah.Dusun')),
            ],
        ),
        migrations.CreateModel(
            name='RT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_rt', models.IntegerField()),
            ],
        ),
    ]
