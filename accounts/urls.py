from django.urls import path
from . import views


urlpatterns = [
    path("addeducation/", views.addeducation, name="addeducation"),
    path("addexperience/", views.addexperience, name="addexperience"),
    path("createprofile/", views.createprofile, name="createprofile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("profiles/", views.profiles, name="profiles"),
    path("register/", views.register, name="register"),
]
