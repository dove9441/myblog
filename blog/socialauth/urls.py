# socialauth/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from socialauth.views import *

app_name = "socialauth"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("login/", login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #아래 것은 여기가 아닌 최상위 urls.py에 적용시켜야 한다.
    #path('social-auth/', include('social_django.urls', namespace="social")),
    path("", testhome, name="testhome"),
]
