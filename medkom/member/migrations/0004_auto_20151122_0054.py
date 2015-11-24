# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20151121_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendidikanterakhir',
            name='status_social_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='agama',
            field=models.ForeignKey(blank=True, to='member.Agama', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='pendonor_darah',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='status_ktp',
            field=models.BooleanField(default=True),
        ),
    ]
