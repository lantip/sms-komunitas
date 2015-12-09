# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20151125_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='alamat_kampung',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'nama_desa', chained_field=b'alamat_desa', blank=True, auto_choose=True, to='wilayah.Kampung', null=True),
        ),
    ]
