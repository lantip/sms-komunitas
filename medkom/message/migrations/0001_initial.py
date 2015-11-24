# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('message', models.CharField(max_length=200)),
                ('persons', models.ManyToManyField(to='member.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('sender', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Moderated'), (1, b'Pending'), (3, b'Spam')])),
                ('resolution', models.IntegerField(null=True, choices=[(0, b'Approved'), (1, b'Decline')])),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='queue',
            field=models.ForeignKey(blank=True, to='message.Queue', null=True),
        ),
    ]
