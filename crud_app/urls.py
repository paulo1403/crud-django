from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import edit_profile, register, change_log_list

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("create/", views.item_create, name="item_create"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    path("<int:pk>/update/", views.item_update, name="item_update"),
    path("<int:pk>/delete/", views.item_delete, name="item_delete"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("register/", register, name="register"),
    path("change-log/", change_log_list, name="change_log_list"),
]
