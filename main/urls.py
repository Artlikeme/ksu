from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.index, name="home"),
    path('',include('titlepage.urls')),
    path('login/', include('registration.urls')),
    path('lk/', include('lk.urls')),
    path('moderation/', include('moderations.urls')),


]
