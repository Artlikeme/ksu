from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from registration.models import UserProfile
from items.models import City, Comment, Item
from .forms import BecomOwnerForm, UserProfileForm


@login_required(login_url='/login/', redirect_field_name='')
def per_cab(request):
    items = Item.objects.filter(author=request.user).order_by('-rating')
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        userprofile = 0

    form = UserProfileForm(request.POST or None,
                           request.FILES or None,
                           initial={
                               'fio': userprofile.fio,
                               'photo': userprofile.photo,
                               'phone_num': userprofile.phone_num,
                           })
    if request.method == 'POST' and form.is_valid():
        profile = UserProfile.objects.get(user=request.user)
        print(form.cleaned_data['fio'])
        try:
            profile.fio = form.cleaned_data['fio']
            profile.phone_num = form.cleaned_data['phone_num']
            profile.photo = form.cleaned_data['photo']
            profile.save()
            messages.success(request, 'Data was changed!')
            return redirect('lk')
        except:
            messages.error(request, 'Invalid try again')
            return redirect('lk')

    comments = Comment.objects.filter(author=request.user).order_by("-id")[0:3]

    city = City.objects.get(id=request.session['my_thing']['foo'])
    context = {
        'items': items,
        'user_p': userprofile,
        'form': form,
        'comments': comments,
        'city': city,
    }
    return render(request=request, template_name="lk/lk.html", context=context)


@login_required(login_url='/login/', redirect_field_name='')
def become_owner(request):
    form = BecomOwnerForm()

    if request.method == 'POST':
        form = BecomOwnerForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user_owner = request.user
            new.save()
            messages.success(request, "Questionnaire added!")
            return redirect('lk')
        messages.error(request, "Invalid information. Try again!")
    context = {
        'form': form,
    }
    return render(request, "lk/become_owner.html", context)
