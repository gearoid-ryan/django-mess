# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_id', models.IntegerField(default=0)),
                ('trade_type', models.CharField(max_length=40)),
                ('trade_maturity', models.DateTimeField(verbose_name=b'Maturity Date')),
                ('trade_value', models.IntegerField(default=0)),
            ],
        ),
    ]
