# Generated by Django 4.0.4 on 2022-04-20 03:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_alter_otpmodel_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 20, 3, 38, 32, 607285, tzinfo=utc)),
        ),
    ]
