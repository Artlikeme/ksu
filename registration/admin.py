from django.contrib import admin

from .models import UserProfile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['fio', 'phone_num','photo']

admin.site.register(UserProfile)
