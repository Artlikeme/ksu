import numpy as np

from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


# Нужно начинать со второго индекса можно удалить вручную первый для main/model
class CategoryItem(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    def __str__(self):
        return self.name


class Item(models.Model):
    rating = models.FloatField(blank=True, default=0)
    category = models.ForeignKey(CategoryItem,
                                 on_delete=models.CASCADE,
                                 verbose_name='category')
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             verbose_name='city')
    item_image = models.ImageField('image', upload_to="items/%Y/%m/%d/")
    item_title = models.CharField('title', max_length=250, default='New item')
    item_description = models.TextField('description', default='Some text')
    item_address = models.CharField('address',
                                    max_length=250,
                                    default='Russia, Moscow, Red square')
    item_mapcode = models.CharField('mapcode', max_length=30)
    item_address_link = models.URLField('address_url')
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               null=True,
                               editable=False,
                               default="None")
    active = models.BooleanField('active', default=False)

    def __str__(self):
        return self.item_title

    def get_absolute_url(self):
        return f"/lk/item/{self.id}"

    @property
    def average_rating(self):
        all_ratings = list(map(lambda x: x.value, self.comments.all()))
        average = np.array(all_ratings).astype(np.float)
        return round(np.average(average), 2)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('rating',)


class FoodBasket(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='food_basked')
    bread = models.IntegerField()
    potato = models.IntegerField()
    sugar = models.IntegerField()
    milk = models.IntegerField()
    eags = models.IntegerField()
    meat = models.IntegerField()
    oil = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class MedPrices(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='MedPrices')
    priem = models.IntegerField()
    covid = models.IntegerField()
    lab_analiz = models.IntegerField()
    days_analiz = models.IntegerField()
    mrt = models.IntegerField()
    days_mrt = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class ParksIvents(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='Parks_Ivents')
    ivents_year = models.IntegerField()
    square = models.IntegerField()
    people_day = models.IntegerField()
    cafes = models.IntegerField()
    prices = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class Kindsgardens(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='Kinds_gardens')
    start_year = models.IntegerField()
    number_of_seats = models.IntegerField()
    ammounts_group = models.IntegerField()
    ammounts_group_teather = models.IntegerField()
    prices_month = models.IntegerField()
    ammont_holidays = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class SchollRate(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='scholl_Rate')
    ege = models.IntegerField()
    number_of_seats = models.IntegerField()
    ammount_class = models.IntegerField()
    ammounts_teather = models.IntegerField()
    prices_month = models.IntegerField()
    ammont_holidays = models.IntegerField()
    rating_city = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class UniversityRate(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='University_Rate')
    ege_sr = models.IntegerField()
    number_of_seats = models.IntegerField()
    facultets = models.IntegerField()
    ammounts_budget = models.IntegerField()
    prices_month_sr = models.IntegerField()
    procent_trud = models.IntegerField()
    rating_city = models.IntegerField()
    rating_russia = models.IntegerField()

    def __str__(self):
        return self.item.item_title


class Comment(models.Model):
    DEFAULT_CHOICES = (
        ('5', 'Отлично'),
        ('4', 'Хорошо'),
        ('3', 'Нормально'),
        ('2', 'Плохо'),
        ('1', 'Ужасно'),
    )
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('active', 'Active'),
    )
    rating_choices = DEFAULT_CHOICES
    value = models.CharField(
        max_length=20,
        verbose_name=('Value'),
        choices=rating_choices,
        blank=True, null=True
    )
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="comments/%Y/%m/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='active')
    active = models.BooleanField(default=True)
    author = models.ForeignKey(to=User,
                               on_delete=models.CASCADE,
                               editable=False)

    def __str__(self):
        return 'Comment by {} mark is {}'.format(self.name, self.value)

    class Meta:
        ordering = ('created',)


class OpeningHours(models.Model):
    WEEKDAYS = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
        (4, ("Thursday")),
        (5, ("Friday")),
        (6, ("Saturday")),
        (7, ("Sunday")),
    ]
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='OpeningHours')
    weekday = models.IntegerField(choices=WEEKDAYS)
    hours = models.CharField(max_length=16, default='с 00:00 до 24:59')

    class Meta:
        ordering = ('weekday',)
        unique_together = ('weekday',)

    def __str__(self):
        return f'Hours for {self.item}'


# HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]

class SpecialDays(models.Model):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             related_name='SpecialDays')
    holiday_date = models.DateField()

    # to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24,
    #                                             null=True, 
    #                                             blank=True)

    def __str__(self):
        return f'Holidays for {self.item}'
