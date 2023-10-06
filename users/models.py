from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='страна', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='Активен')
    code = models.CharField(default=None, verbose_name='код верификации', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []