# Generated by Django 4.2.4 on 2023-10-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_accesorios_ropa_zapatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='ropa',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='zapatos',
            name='precio',
        ),
        migrations.AlterField(
            model_name='accesorios',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
