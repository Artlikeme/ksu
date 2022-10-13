from django import forms
from .models import Cities_dropbox

class SelectCityForm(forms.ModelForm):
    class Meta:
        model = Cities_dropbox
        fields = '__all__'
