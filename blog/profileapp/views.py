from django.shortcuts import render
from django.views.generic import *
from profileapp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from profileapp.decorators import *
from django.contrib.auth.models import User
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy("accountapp:detail")
    template_name = 'profileapp/create.html' 
    
    
    # def form_valid(self, form):
    #     return super().form_valid(form) 하면 기존과 같음.(원래 클래스 내장 함수임)
    
    def form_valid(self, form):
        temp_profile = form.save(commit=False) #입력받음 form을 임시로 저장한다(commit에서 보내지 않음으로 설정)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form) #이렇게 하면 models에서 정의했던 멤버변수 user를 입력받지 않아서 생기는 오류가 해결됨 근데 왜 해결되지??
    
    
    #ProfileCreation 이후 url에 pk를 같이 넘겨주기 위해 내장 함수를 수정
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk' : self.object.user.pk})
    
    

    
@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView): #사실 Update는 기존 내용 수정이기 때문에 CreateView와 거의 유사하다.
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm #이것도 그대로 쓴다 
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk' : self.object.user.pk})
    
    

class ProfileListView(ListView):
    model = Profile
    context_object_name = 'target_profile'
    template_name = 'profileapp/list.html'
    paginate_by = 15
    
    
    def get_context_data(self, **kwargs):
        object_list = User.objects.all()
        return super(ProfileListView,self).get_context_data(object_list=object_list,**kwargs)
    #get_context_data를 오버라이딩해줘야 템플릿에 데이터가 같이 넘어간다.
    #profileapp.models에서 이미 User와 ForeignKey로 연결을 해놓아서 유저 데이터를 넘길 수 있다.
    
    
    
    #제발 View 만들면 urls.py에서 만들자