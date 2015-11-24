# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nonmember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis_kelamin', models.IntegerField(default=0, choices=[(0, b'Laki Laki'), (1, b'Perempuan')])),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('nama_panggilan', models.CharField(max_length=20, blank=True)),
                ('no_handphone', models.CharField(max_length=15, blank=True)),
                ('jabatan', models.CharField(max_length=255, blank=True)),
                ('nama_dinas', models.CharField(max_length=255)),
                ('wilayah', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Non Member',
                'verbose_name_plural': 'Non Member',
            },
        ),
    ]
