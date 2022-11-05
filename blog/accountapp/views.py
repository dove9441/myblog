from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다
from django.http import HttpResponseRedirect #이것도 따로 해야 한다..
from django.urls import reverse, reverse_lazy


# 모델도 import해야 한다.
from accountapp.models import HelloWorld

# CRUD View class 이용한 CreateView 만들기
from django.views.generic import *  #CreateView, DetailView 등 불러오기
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here. 

def hello_world(request):
    #return HttpResponse("hello world!") #HttpResponse를 직접 리턴
    #form의 method 값 get/post 따라서 요청을 나눈다
    if request.method=="POST":
        temp = request.POST.get('hello_world_input') #request의 post 요청 (하지만 대문자로 써야 한다)에서  input 태그의 name속성값이 hello_world_input인 것의 데이터를 가져와라
        
        
        #DB에 저장하기 
        new_hello_world = HelloWorld() #인스턴스 생성 (객체 타입은 HelloWorld이다)
        new_hello_world.text = temp
        new_hello_world.save() #DB에 new_hello_world 인스턴스를 저장
        
        #DB에서 불러오기
        
        hello_world_list = HelloWorld.objects.all() #HelloWorld 클래스 타입 내장 기본 함수여서 HelloWorld.을 쓰나보다?
        
        return HttpResponseRedirect(reverse('accountapp:hello_world')) #/accountapp/urls.py의 app_name을 입력하면 알아서 urlpatterns의 경로를 참고하여 account/hello_world로 변환된다.
    
    
        #return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) #/accountapp/hello_world가 아니다. 앞에 /는 꼭 빼야 한다 context는 보내줄 데이터다

    
    
    

    
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #reverse_lazy는 reverse와 같지만 reverse는 function에서, reverse_lazy는 class에서 사용한다.
    template_name = 'accountapp/create.html'
    
    
    
class AccountDetailView(DetailView):
    model = User #U 대문자이다..
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
    
    
    
#처음 이렇게 만들고 root에서 setting.py에서 템플릿 경로 추가
#렌더링할 html경로를 적어주는 것
#여기서 만들고 최초 폴더의 urls.py에서 라우팅



