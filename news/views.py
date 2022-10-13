from django.shortcuts import render, redirect

from items.models import City
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    city = City.objects.get(id = request.session['my_thing']['foo'])
    news = Articles.objects.filter(city = request.session['my_thing']['foo']).order_by('-date')
    return render(request, 'news/news_home.html', {'news': news,'city':city})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была заполнена неверно'


    form = ArticlesForm()
    city = City.objects.get(id = request.session['my_thing']['foo'])

    data = {
        'form': form,
        'error':error,
        'city':city
    }
    return render(request, 'news/create.html', data)