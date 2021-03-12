from django.urls import path
from .views import login_view, logout_view, register_view, profile_view, edit_profile_view


urlpatterns = [
    path("login", login_view, name="login_view"),
    path("logout", logout_view, name="logout_view"),
    path("register/", register_view, name='register'),
    path("profile/", profile_view, name='profile_view'),
    path("edit_profile/", edit_profile_view, name='edit_profile_view')
]
