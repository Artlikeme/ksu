from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import SelectCityForm
from .models import City

# Create your views here.
def titlepage(request):
    object_list = City.objects.all()
    
    form = SelectCityForm()
    if request.GET.get('dropbox',False):
        my_thing = {'foo' : request.GET.get('dropbox',False)}
        request.session['my_thing'] = my_thing
        return redirect("home")
    else:
        if request.method == 'GET' and  City.objects.filter(id=request.GET.get('dropbox',False))[::-1] != []:
            messages.success(request, "Для этого города еще не добавлен раздел")
    return render(request, 'titlepage/breh.html',
    context = {
        'object_list':object_list,
        'form':form,
    })

    