from django import forms
from items.models import Item
from lk.models import OwnerQuestionnaire


class ModerationItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields =('active',)

class ModerationOwnerForm(forms.ModelForm):
    class Meta:
        model = OwnerQuestionnaire
        fields =('active',)
