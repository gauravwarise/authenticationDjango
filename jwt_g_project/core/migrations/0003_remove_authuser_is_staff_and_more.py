# Generated by Django 4.2.4 on 2023-12-09 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_authuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='last_login',
        ),
    ]