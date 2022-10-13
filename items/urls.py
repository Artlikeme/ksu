from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


# item/
urlpatterns = [
    path('additem/', views.add_item, name="additem"),
    path('<int:pk>', views.ItemDetailView.as_view(), name="itemview"),
    path('update/<int:pk>', views.ItemUpdateView.as_view(), name="itemupdate"),
    path('delitem/<int:pk>', views.ItemDeleteView.as_view(), 
        name="itemudelete"),
]
