from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.per_cab, name="lk"),
    # path('',views.UserProfileUpdateView.as_view(),name="updateUser"),
    path('item/',include('items.urls')),
    path('becomeowner/',views.become_owner, name="becomeowner"),
]
