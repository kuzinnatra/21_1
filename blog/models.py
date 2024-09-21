from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    # заголовок;
    # slug(реализоватьчерезCharField);
    # содержимое;
    # превью(изображение);
    # датасоздания;
    # признакпубликации;
    # количествопросмотров
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
