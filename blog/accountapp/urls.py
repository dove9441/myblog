from django.contrib import admin
from django.urls import path, include #include 추가
from accountapp.views import * #views.py의 funtion, class view들을 불러온다
 
#urls.path(route, view, kwrags=None, name=None,Pattern=)

app_name='accountapp' #하면 좋음. 계속 쳐야 하니 그냥 이름 변수에 저장


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'), #class형 view는 이후에 .as_view()를 적어야 한다.

]