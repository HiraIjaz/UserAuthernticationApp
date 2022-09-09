from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("updateprofile/", views.updateprofile, name="updateprofile"),
]
