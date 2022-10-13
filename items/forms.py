from dataclasses import fields
from email.policy import default
from django.forms import ModelForm
from django import forms

from .models import FoodBasket, Item, Comment, Kindsgardens, MedPrices, OpeningHours, ParksIvents, SchollRate, SpecialDays, UniversityRate


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('item_title','item_description',
                'item_address','item_address_link',
                'item_mapcode','item_image',
                'category','city')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('description','image','value')


class OpeningHoursForm(ModelForm):
    class Meta:
        model = OpeningHours
        fields = ('weekday','hours')


class SpecialDaysForm(ModelForm):
    class Meta:
        model = SpecialDays
        fields = ('holiday_date',)


class FoodBaskedForm(ModelForm):
    class Meta:
        model = FoodBasket
        fields = ('bread','potato','sugar','milk','eags','meat','oil')


class FormCalculate(forms.Form):
    first = forms.IntegerField(required=False,initial=1)
    second = forms.IntegerField(required=False,initial=1)
    third = forms.IntegerField(required=False,initial=1)
    fourth = forms.IntegerField(required=False,initial=1)
    fifth = forms.IntegerField(required=False,initial=1)
    sixth = forms.IntegerField(required=False,initial=1)
    seventh = forms.IntegerField(required=False,initial=1)


class MedPricesForm(ModelForm):
    class Meta:
        model = MedPrices
        fields = ('priem','covid','lab_analiz','days_analiz','mrt','days_mrt')


class ParksIventsForm(ModelForm):
    class Meta:
        model = ParksIvents
        fields = ('ivents_year','square','people_day','cafes','prices')
 

class KindsgardensForm(ModelForm):
    class Meta:
        model = Kindsgardens
        fields = ('start_year','number_of_seats','ammounts_group','ammounts_group_teather','ammont_holidays','prices_month')


class SchollRateForm(ModelForm):
    class Meta:
        model = SchollRate
        fields = ('ege','number_of_seats','ammount_class','ammounts_teather','ammont_holidays','prices_month','rating_city')


class UniversityRateForm(ModelForm):
    class Meta:
        model = UniversityRate
        fields = ('ege_sr','number_of_seats','facultets','ammounts_budget','prices_month_sr','procent_trud','rating_city','rating_russia')
