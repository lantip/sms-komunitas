# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20151122_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agama',
            name='agama',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='golongandarah',
            name='golongan_darah',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hubungankeluarga',
            name='hubungan_keluarga',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jurusan',
            name='jurusan',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pekerjaan',
            name='pekerjaan',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pendidikanterakhir',
            name='pendidikan_terakhir',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='statusperkawinan',
            name='status_perkawinan',
            field=models.CharField(max_length=200),
        ),
    ]
