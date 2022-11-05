from django.contrib import admin
from django.urls import path, include #include 추가
from accountapp.views import * #views.py의 funtion, class view들을 불러온다
from django.contrib.auth.views import LoginView, LogoutView  #django 내장 Login/Logout View를 불러온다.

#urls.path(route, view, kwrags=None, name=None,Pattern=)

app_name='accountapp' #하면 좋음. 계속 쳐야 하니 그냥 이름 변수에 저장


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), #로그인 view는 따로 템플릿 설정. 괄호 위치 주의. 
    path('logout/', LogoutView.as_view(), name='logout'), #로그아웃 뷰는 없어도 됨.
    
    path('create/', AccountCreateView.as_view(), name='create'), #class형 view는 이후에 .as_view()를 적어야 한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), #<int:pk>는 접속 사용자 각각의 개별 구별자이다 (primary key)
 
]