from django.db import models
from django.contrib.auth.models import User


class OwnerQuestionnaire(models.Model):
    user_owner = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                verbose_name='user_owner')
    name_organisation = models.CharField('name_organ',max_length=255)
    text_questionnaire = models.TextField('text_questionnaire')
    active = models.BooleanField('active',default=False)

    def  __str__(self):
        return self.user_owner.email