from django.forms import ModelForm

from lk.models import OwnerQuestionnaire
from registration.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fio','phone_num','photo')

class BecomOwnerForm(ModelForm):
    class Meta:
        model = OwnerQuestionnaire
        fields = ('name_organisation','text_questionnaire')
