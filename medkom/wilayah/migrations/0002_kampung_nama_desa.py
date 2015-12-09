# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilayah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kampung',
            name='nama_desa',
            field=models.ForeignKey(default=1, to='wilayah.Desa'),
            preserve_default=False,
        ),
    ]
