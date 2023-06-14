import datetime

from django.db import models
from django.urls import reverse

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='заголовок')
    blog_slug = models.CharField(max_length=100, verbose_name='slug')
    blog_content = models.TextField(verbose_name='содержимое', **NULLABLE)
    blog_preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    blog_created_at = models.DateField(verbose_name='создан', default=datetime.date.today)
    blog_is_publicated = models.BooleanField(verbose_name='опубликован', default=False)
    blog_views_count = models.BigIntegerField(verbose_name='количество просмотров', default=0)

    # def get_absolute_url(self):
    #     return reverse('blogs_item', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.blog_title}\nСоздан: {self.blog_created_at}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('blog_title',)
