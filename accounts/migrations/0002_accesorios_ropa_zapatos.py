# Generated by Django 4.2.4 on 2023-10-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('talla', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imagen', models.ImageField(upload_to='accesorios/')),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('talla', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imagen', models.ImageField(upload_to='ropa/')),
            ],
        ),
        migrations.CreateModel(
            name='Zapatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('talla', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imagen', models.ImageField(upload_to='zapatos/')),
            ],
        ),
    ]
