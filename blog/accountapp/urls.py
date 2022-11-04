from django.contrib import admin
from django.urls import path, include #include 추가
from accountapp.views import hello_world #??

#urls.path(route, view, kwrags=None, name=None,Pattern=)

app_name='hello_world' #하면 좋음. 계속 쳐야 하니 그냥 이름 변수에 저장


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]