# Generated by Django 3.0.5 on 2020-10-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstoretia', '0009_auto_20201007_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas',
            name='fuel_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='markdown1',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='markdown2',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='markdown3',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='markdown4',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='markdown5',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristicas',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
    ]