from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from items.models import Item
from lk.models import OwnerQuestionnaire
from moderations.forms import ModerationItemForm, ModerationOwnerForm


def moderation(request):
    return render(request, 'moderations/moderations.html')


def moderation_owners(request):
    form = ModerationOwnerForm()
    try:
        obj = OwnerQuestionnaire.objects.filter(active=False).order_by('-id')[0]
    except IndexError:
        obj = 0

    s = OwnerQuestionnaire.objects.filter(active=False).count()

    if request.method == 'POST':
        form = ModerationOwnerForm(request.POST)
        if form.is_valid:
            if form.data.get("active") == "on":
                owner = OwnerQuestionnaire.objects.get(id=obj.id)
                owner.active = True
                new_group = Group.objects.get(name='owner')
                owner.user_owner.groups.add(new_group)
                owner.save()
            return redirect('moderation_owners')

    context = {
        'item': obj,
        'count': s,
        'form': form,
    }
    return render(request, 'moderations/moderation_owners.html', context)


def moderation_items(request):
    form = ModerationItemForm()
    try:
        obj = Item.objects.filter(active=False).order_by('-id')[0]
    except IndexError:
        obj = 0
    s = Item.objects.filter(active=False).count()

    if request.method == 'POST':
        form = ModerationItemForm(request.POST)
        if form.is_valid:
            item = Item.objects.get(id=obj.id)
            item.active = True if form.data.get("active") == "on" else False
            item.save()
            return redirect('moderation_items')
    context = {
        'item': obj,
        'count': s,
        'form': form,
    }
    return render(request, 'moderations/moderation_items.html', context)
