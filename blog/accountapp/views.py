from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다
from django.http import HttpResponseRedirect #이것도 따로 해야 한다..
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy


# 모델도 import해야 한다.
#from accountapp.models import HelloWorld

# CRUD View class 이용한 CreateView 만들기
from django.views.generic import *  #CreateView, DetailView 등 불러오기
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# UpdateView에서 수정된 form_class를 적용하기 위해 불러옴. 기본 경로는 blog이기 때문에 accountapp.forms이다.
from accountapp.forms import AccountUpdateForm


#decorator import
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import *

# Create your views here. 

# decorator 배열
has_ownership=[login_required,account_ownership_required]

#MultipleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article


# @login_required #모듈을 통해 불러온다
# def hello_world(request):
    
#     # 로그인 인증
#    	#return HttpResponse("hello world!") #HttpResponse를 직접 리턴
#         #form의 method 값 get/post 따라서 요청을 나눈다
#     if request.method=="POST":
#         temp = request.POST.get('hello_world_input') #request의 post 요청 (하지만 대문자로 써야 한다)에서  input 태그의 name속성값이 hello_world_input인 것의 데이터를 가져와라


#         #DB에 저장하기 
#         new_hello_world = HelloWorld() #인스턴스 생성 (객체 타입은 HelloWorld이다)
#         new_hello_world.text = temp
#         new_hello_world.save() #DB에 new_hello_world 인스턴스를 저장

#         #DB에서 불러오기

#         hello_world_list = HelloWorld.objects.all() #HelloWorld 클래스 타입 내장 기본 함수여서 HelloWorld.을 쓰나보다?

#         return HttpResponseRedirect(reverse('accountapp:hello_world')) #/accountapp/urls.py의 app_name을 입력하면 알아서 urlpatterns의 경로를 참고하여 account/hello_world로 변환된다.


#         #return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
#     else:
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) #/accountapp/hello_world가 아니다. 앞에 /는 꼭 빼야 한다 context는 보내줄 데이터다

    

    
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login') #reverse_lazy는 reverse와 같지만 reverse는 function에서, reverse_lazy는 class에서 사용한다.
    template_name = 'accountapp/create.html'
    
    
    
class AccountDetailView(DetailView,MultipleObjectMixin):
    model = User #U 대문자이다..
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object()) #해당 project에 속해있는 articles를 가져오는 건데 이해는 잘 안 된다. Accountapp에서는 해당 account의 게시물이다.
        return super(AccountDetailView,self).get_context_data(object_list=object_list,**kwargs)
    


    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')#클래스 안의 메서드에서 decorator를 사용하려면 이렇게 해야 한다. #사용자 정의 decorator (accountapp/decorators.py에 있음)
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:detail') 
    template_name = 'accountapp/update.html'
    
    
        
        
    
    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView): #CreateView, DetailView(Read이지만 장고에서는 Detail이다), DeleteView를 상속해서 기능이 추가된 새로운 뷰를 정의하는 것이다.
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    
    
    
    
    
    
###################PROFILEAPP##########################
    

    
    
    
    
    
#처음 이렇게 만들고 root에서 setting.py에서 템플릿 경로 추가
#렌더링할 html경로를 적어주는 것
#여기서 만들고 최초 폴더의 urls.py에서 라우팅

# 1. 앱 만들기 (python manage.py startapp '앱 이름')
# 2. settings.py에 앱 추가
# 3. urls.py(프로젝트 폴더)에서 경로 지정
# 4. 앱 내부에 urls.py 만들기
# 5. 모델 만들기
# 6. form 만들기
# 7. python manage.py makemigrations 이후 python manage.py migrate를 해줘야 db와 연동이 된다.
# 8. View 만들기

# !! View 만드는 순서 : 
# 1. View.py에 class나 function 만들기 (template_name 등 추가)
# 2. urls.py에 path 추가하기
# 3. template 폴더에서 html 파일 작성하기

