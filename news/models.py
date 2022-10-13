from django.db import models
from django.utils import timezone

from items.models import City



class Articles(models.Model):
    city = models.ForeignKey(City,
                                on_delete=models.CASCADE,
                                verbose_name='city')
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации',default=timezone.now)

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name ='Новость'
        verbose_name_plural ='Новости'