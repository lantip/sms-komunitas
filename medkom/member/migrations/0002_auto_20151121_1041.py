# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='atap',
            field=models.ForeignKey(blank=True, to='member.Atap', null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='dinding',
            field=models.ForeignKey(blank=True, to='member.Dinding', null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='lantai',
            field=models.ForeignKey(blank=True, to='member.Lantai', null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='status_listrik',
            field=models.ForeignKey(blank=True, to='member.StatusListrik', null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='status_rumah',
            field=models.ForeignKey(blank=True, to='member.StatusRumah', null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='sumber_air_minum',
            field=models.ForeignKey(blank=True, to='member.SumberAirMinum', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='hubungan_keluarga',
            field=models.ForeignKey(blank=True, to='member.HubunganKeluarga', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='status_perkawinan',
            field=models.ForeignKey(blank=True, to='member.StatusPerkawinan', null=True),
        ),
    ]
