from django.db import models

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


    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = (
            "name",
            "price",
        )

    def __str__(self):
        return f"{self.name}"
