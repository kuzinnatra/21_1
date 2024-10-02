NULLABLE = {"blank": True, "null": True}
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Изображение (превью)",
        help_text="загрузите изображение",
        **NULLABLE,
    )
    date_create = models.DateField(
        **NULLABLE,
        verbose_name="Дата публикации",
        help_text="Укажите дату публикации",

    )

    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug',null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
