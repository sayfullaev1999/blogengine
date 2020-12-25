from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """ Модель для постов """
    title = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='URL'
    )
    body = models.TextField(
        blank=True,
        db_index=True,
        verbose_name='Тело'
    )
    date_pub = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
