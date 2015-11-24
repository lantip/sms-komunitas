# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20151121_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='kepemilikan_wc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='family',
            name='nomor_kk',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='nomor_quesioner',
            field=models.CharField(max_length=6, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='penerima_jamsos',
            field=models.BooleanField(default=False),
        ),
    ]
