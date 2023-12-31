# Generated by Django 4.2.4 on 2023-12-08 07:05

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_created=True, db_column='date_joined', null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('username', models.CharField(db_column='username', max_length=255, unique=True)),
                ('password', models.CharField(db_column='password', max_length=255, unique=True)),
                ('email', models.CharField(db_column='email', max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, db_column='first_name', max_length=255)),
                ('last_name', models.CharField(blank=True, db_column='last_name', max_length=255)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('groups', models.ManyToManyField(related_name='auth_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='auth_users', to='auth.permission')),
            ],
            options={
                'db_table': 'custom_auth_user',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
