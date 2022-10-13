from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_reg, name="login"),
    path('registration/', views.signup, name="signup"),
    path('logout/', views.logout_request, name="logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    # path("edit/", views.edit, name="edit"),
]
