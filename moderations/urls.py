from django.urls import path
from . import views

urlpatterns = [
    path('', views.moderation, name="moderation"),
    path('owners/', views.moderation_owners, name="moderation_owners"),
    path('items/', views.moderation_items, name="moderation_items"),


]
