# Generated by Django 3.0.5 on 2020-10-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstoretia', '0003_auto_20201006_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas',
            name='cpi',
            field=models.BigIntegerField(default=None),
        ),
    ]
