# from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from django import forms
from main.models import Cat_item_dropbox

class SelectCategForm(forms.ModelForm):
    class Meta:
        model = Cat_item_dropbox
        fields = '__all__'
