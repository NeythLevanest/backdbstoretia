# Generated by Django 3.0.5 on 2020-10-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.IntegerField(default=None)),
                ('date', models.DateField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fuel_price', models.DecimalField(decimal_places=3, max_digits=3)),
                ('markdown1', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('markdown2', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('markdown3', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('markdown4', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('markdown5', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('cpi', models.IntegerField(default=None)),
                ('unemployme', models.IntegerField(default=None)),
                ('isHoliday', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tiendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.IntegerField(default=None)),
                ('type', models.CharField(default=None, max_length=1)),
                ('size', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.IntegerField(default=None)),
                ('departamento', models.IntegerField(default=None)),
                ('date', models.DateField()),
                ('weekly_sales', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('isHoliday', models.BooleanField(default=False)),
            ],
        ),
    ]
