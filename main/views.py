from django.shortcuts import render

from items.models import City, Item
from main.forms import SelectCategForm
from news.models import Articles


def index(request):
    cat_item = Item.objects.filter(city=request.session['my_thing']['foo'])[::-1]
    form = SelectCategForm()
    if request.GET.get('dropbox', False) == "1":
        cat_item = Item.objects.all()[::-1]
    else:
        if request.method == 'GET' and Item.objects.filter(category=request.GET.get('dropbox', False))[::-1] != []:
            cat_item = Item.objects.filter(city=request.session['my_thing']['foo'],
                                           category=request.GET.get('dropbox', False))[::-1]
        else:
            cat_item = Item.objects.filter(city=request.session['my_thing']['foo'])[::-1]
    articles_anonces = Articles.objects.filter(city=request.session['my_thing']['foo']).order_by('-date')[0:2]
    city = City.objects.get(id=request.session['my_thing']['foo'])
    context = {
        'catitem': cat_item,
        'form': form,
        'article': articles_anonces,
        'city': city,
    }
    return render(request, 'main/index.html', context)
