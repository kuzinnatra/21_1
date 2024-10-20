from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """создаем модель категории"""

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="введите описание категории", **NULLABLE
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """создаем модель продукты(товары)"""

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование товара",
        help_text="введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="введите описание товара", **NULLABLE
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение (превью)",
        help_text="загрузите изображение товара",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="выберите категорию товара",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="введите цену покупки (целое число)"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Дата создания (записи в БД)"
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения (записи в БД)",
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='владелец',
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Опубликовать запись"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ("name", "price")
        permissions = [
            ("can_edit_is_published", "can edit is_published"),
            ("can_edit_description", "can edit description"),
            ("can_edit_category", "can edit category")
        ]

    def __str__(self):
        return f"{self.name}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="продукт",
    )

    num_version = models.IntegerField(
        verbose_name="Номер версии", help_text="введите номер версии (целое число)")

    name_version = models.CharField(
        max_length=50,
        verbose_name="Название версии",
        help_text="введите название версии",
        **NULLABLE,
    )

    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"

    def __str__(self):
        return self.name_version