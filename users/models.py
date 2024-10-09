from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE, help_text="Введите номер телефона")
    country = models.CharField(max_length=50, verbose_name="Страна", **NULLABLE, help_text="Введите страну")
    avatar = models.ImageField(upload_to="users/avatar", verbose_name="Аватар", **NULLABLE, help_text="Загрузите свою аватарку")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Поьзователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"

