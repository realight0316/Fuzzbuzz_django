from django.urls import path, include
from django.urls.resolvers import URLPattern
from fuzzbuzz_app1 import views

from fuzzbuzz_app1 import views as appviews
from fuzzbuzz_django import views as projviews

app_name = "fuzzbuzz_app1"

urlpatterns = [
    path("login/", appviews.web_login, name="login"),
    path("logout/", appviews.web_logout, name="logout"),
    path("signup/", appviews.web_signup, name="signup"),
    path("chart/", appviews.web_chart, name="chart"),
]
