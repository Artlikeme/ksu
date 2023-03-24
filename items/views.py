from datetime import date
from urllib import response
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from numpy import array

from registration.models import UserProfile

from .models import City, Comment, FoodBasket, Item, Kindsgardens, MedPrices, OpeningHours, ParksIvents, SchollRate, \
    SpecialDays, UniversityRate
from items.forms import FoodBaskedForm, FormCalculate, ItemForm, CommentForm, KindsgardensForm, MedPricesForm, \
    OpeningHoursForm, ParksIventsForm, SchollRateForm, SpecialDaysForm, UniversityRateForm


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            messages.success(request, "Item added!")
            return redirect('lk')
        messages.error(request, "Invalid information. Try again!")
    else:
        form = ItemForm()
    city = City.objects.get(id=request.session['my_thing']['foo'])

    return render(request, "items/add_item.html", {'form': form, 'city': city})


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/det_view_item.html'
    context_object_name = 'itemview'

    def get_context_data(self, **kwargs):
        formpk = self.kwargs['pk']
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        form_hours = OpeningHoursForm()
        form_holidays = SpecialDaysForm()
        comments = Comment.objects.filter(item=formpk)
        hours = OpeningHours.objects.filter(item=
                                            formpk).order_by('weekday')
        holidays = SpecialDays.objects.filter(item=formpk)
        try:
            counter = holidays[0]
            for i in holidays:
                if i.holiday_date < counter.holiday_date:
                    counter = i
            counter = counter.holiday_date
        except:
            counter = '0000-00-00'

        item_for_com = Item.objects.get(id=formpk)
        author_item = UserProfile.objects.get(user=item_for_com.author)

        try:
            rating = item_for_com.average_rating
            item_for_com.rating = rating
            item_for_com.save()
        except IntegrityError:
            rating = 0
            item_for_com.rating = rating
            item_for_com.save()

        # продуктовая корзина
        foodbasket_first = 1
        foodbasket_second = 1
        foodbasket_third = 1
        foodbasket_fourth = 1
        foodbasket_fifth = 1
        foodbasket_sixth = 1
        foodbasket_seventh = 1
        self.request.session['fb_flag'] = 0
        if FormCalculate(self.request.GET) and self.request.GET.get('first') != None:
            foodbasket_first = self.request.GET.get('first')
            foodbasket_second = self.request.GET.get('second')
            foodbasket_third = self.request.GET.get('third')
            foodbasket_fourth = self.request.GET.get('fourth')
            foodbasket_fifth = self.request.GET.get('fifth')
            foodbasket_sixth = self.request.GET.get('sixth')
            foodbasket_seventh = self.request.GET.get('seventh')
            self.request.session['fb_flag'] = 1

        foodbasket = 0
        if Item.objects.get(id=formpk).category.name == 'Магазины':
            try:
                foodbasket = FoodBasket.objects.filter(item=formpk).order_by('-id')[0]
                res = 0
                res += (foodbasket.bread * int(foodbasket_first))
                res += (foodbasket.potato * int(foodbasket_second))
                res += (foodbasket.milk * int(foodbasket_third))
                res += (foodbasket.meat * int(foodbasket_fourth))
                res += (foodbasket.oil * int(foodbasket_fifth))
                res += (foodbasket.sugar * int(foodbasket_sixth))
                res += (foodbasket.eags * int(foodbasket_seventh))

            except:
                res = 0
                foodbasket = 0
        form_foodbasket = FoodBaskedForm()

        # мед учреждения
        medprices = 0
        if Item.objects.get(id=formpk).category.name == 'Медицинские учреждения':
            try:
                medprices = MedPrices.objects.filter(item=formpk).order_by('-id')[0]
            except:
                medprices = 0
        form_medprices = MedPricesForm()

        # парки
        parkivents = 0
        if Item.objects.get(id=formpk).category.name == 'Парки':
            try:
                parkivents = ParksIvents.objects.filter(item=formpk).order_by('-id')[0]
            except:
                parkivents = 0
        form_parkivents = ParksIventsForm()

        # садики
        kindsgardens = 0
        if Item.objects.get(id=formpk).category.name == 'Детские сады':
            try:
                kindsgardens = Kindsgardens.objects.filter(item=formpk).order_by('-id')[0]
            except:
                kindsgardens = 0
        form_kindsgardens = KindsgardensForm()

        # школы
        schollRate = 0
        if Item.objects.get(id=formpk).category.name == 'Школы':
            try:
                schollRate = SchollRate.objects.filter(item=formpk).order_by('-id')[0]
            except:
                schollRate = 0
        form_schollRate = SchollRateForm()

        # универы
        universityrate = 0
        if Item.objects.get(id=formpk).category.name == 'Университеты':
            try:
                universityrate = UniversityRate.objects.filter(item=formpk).order_by('-id')[0]
            except:
                universityrate = 0
        form_universityrate = UniversityRateForm()

        city = City.objects.get(id=self.request.session['my_thing']['foo'])

        context['fb_flag'] = self.request.session['fb_flag']
        context['city'] = city
        context['counter_specialdays'] = counter
        context['form'] = form
        context['author_item'] = author_item.fio
        context['form_hours'] = form_hours
        context['form_holidays'] = form_holidays
        context['form_foodbasket'] = form_foodbasket
        context['form_medprices'] = form_medprices
        context['form_parkivents'] = form_parkivents
        context['form_kindsgardens'] = form_kindsgardens
        context['form_schollRate'] = form_schollRate
        context['form_universityrate'] = form_universityrate
        context['FormCalculate'] = FormCalculate()
        context['hours'] = hours
        context['holidays'] = holidays
        context['comment'] = comments
        context['rating'] = rating
        context['foodbasket'] = foodbasket
        context['medprices'] = medprices
        context['parkivents'] = parkivents
        context['kindsgardens'] = kindsgardens
        context['schollRate'] = schollRate
        context['universityrate'] = universityrate

        if Item.objects.get(id=formpk).category.name == 'Магазины':
            context['res'] = res

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        form_hours = OpeningHoursForm(request.POST)
        form_foodbasket = FoodBaskedForm(request.POST)
        form_holidays = SpecialDaysForm(request.POST)
        form_medprices = MedPricesForm(request.POST)
        form_parkivents = ParksIventsForm(request.POST)
        form_kindsgardens = KindsgardensForm(request.POST)
        form_schollRate = SchollRateForm(request.POST)
        form_universityrate = UniversityRateForm(request.POST)

        formpk = self.kwargs['pk']
        item = Item.objects.get(id=formpk)

        if form.is_valid() and not request.user.is_authenticated:
            new_item = form.save(commit=False)
            new_item.name = request.user.username
            new_item.author = request.user
            new_item.item = item
            new_item.save()
            return redirect(f'/lk/item/{formpk}')

        elif form_hours.is_valid():
            form_hours = form_hours.save(commit=False)
            form_hours.item = item
            form_hours.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_holidays.is_valid():
            form_holidays = form_holidays.save(commit=False)
            form_holidays.item = item
            form_holidays.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_foodbasket.is_valid():
            form_foodbasket = form_foodbasket.save(commit=False)
            form_foodbasket.item = item
            form_foodbasket.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_medprices.is_valid():
            form_medprices = form_medprices.save(commit=False)
            form_medprices.item = item
            form_medprices.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_parkivents.is_valid():
            form_parkivents = form_parkivents.save(commit=False)
            form_parkivents.item = item
            form_parkivents.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_kindsgardens.is_valid():
            form_kindsgardens = form_kindsgardens.save(commit=False)
            form_kindsgardens.item = item
            form_kindsgardens.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_schollRate.is_valid():
            form_schollRate = form_schollRate.save(commit=False)
            form_schollRate.item = item
            form_schollRate.save()

            return redirect(f'/lk/item/{formpk}')

        elif form_universityrate.is_valid():
            form_universityrate = form_universityrate.save(commit=False)
            form_universityrate.item = item
            form_universityrate.save()

            return redirect(f'/lk/item/{formpk}')

        else:
            messages.error(request, "Incorrrect")
            return redirect(f'/lk/item/{formpk}')


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = 'items/add_item.html'
    context_object_name = 'updateitem'
    form_class = ItemForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = "/lk/"
    template_name = 'items/del_item.html'
    context_object_name = 'delitem'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
