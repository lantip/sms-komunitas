# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spammers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_handphone', models.CharField(max_length=200)),
                ('time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Spammer',
                'verbose_name_plural': 'Spammer',
            },
        ),
    ]
