# Generated by Django 5.1.3 on 2024-11-24 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_bancario_app', '0002_rename_conta_movimento_idconta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimento',
            name='horaMovimento',
        ),
        migrations.AlterField(
            model_name='movimento',
            name='dataMovimento',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 24, 21, 5, 15, 100700)),
        ),
    ]
