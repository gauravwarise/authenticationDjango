# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission




class AuthUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, db_column='username', null=False)
    password = models.CharField(max_length=255, unique=True, db_column='password', null=False)
    email = models.CharField(max_length=255, unique=True, db_column='email', null=False)
    first_name = models.CharField(max_length=255, blank=True, db_column='first_name', null=False)
    last_name = models.CharField(max_length=255, blank=True, db_column='last_name', null=False)
    date_joined = models.DateTimeField(auto_created=True, null=True, db_column='date_joined')
    is_active = models.BooleanField(default=True, db_column='is_active')

    USERNAME_FIELD = 'username'

    class Meta:
        managed = True
        db_table = "custom_auth_user"

    def save(self, *args, **kwargs):
        super(AuthUser, self).save(*args, **kwargs)

    groups = models.ManyToManyField(Group, related_name='auth_users')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_users')
