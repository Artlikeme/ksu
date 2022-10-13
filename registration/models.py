from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    fio = models.CharField('fio',max_length=255,default='Default')
    phone_num = models.CharField('phone_num',
                                max_length=13,
                                blank=True, 
                                null=True)
    photo = models.ImageField('image',
                            upload_to="Users/%Y/%m/%d/",
                            blank=True, 
                            null=True, 
                            default='images.png')
    # user = models.OneToOneField(User,on_delete=models.CASCADE,
    #                            related_name='userprofile')
    user = models.ForeignKey(User, 
                            on_delete=models.CASCADE,
                            related_name='userprofile')

    def __str__(self):
        return f'Profile for user {self.user.username}'


    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
