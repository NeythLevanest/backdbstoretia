# Generated by Django 3.0.5 on 2020-10-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstoretia', '0008_auto_20201007_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiendas',
            name='size',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
    ]
