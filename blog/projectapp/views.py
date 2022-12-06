from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from projectapp.forms import *
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article
from subscribeapp.models import Subscription

# Create your views here.
@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    
    
    def get_success_url(self):
        return reverse_lazy('projectapp:detail', kwargs={'pk' : self.object.pk})
    
    
class ProjectDetailView(DetailView, MultipleObjectMixin): #믹스인 사용
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    
    paginate_by = 25
    
    def get_context_data(self, **kwargs): #템플릿에게 데이터를 전달하기 위해 오버라이딩
        project = self.object
        user = self.request.user
        
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)
            
        object_list = Article.objects.filter(project=self.get_object()) #해당 project에 속해있는 articles를 가져오는 건데 이해는 잘 안 된다.
        return super(ProjectDetailView,self).get_context_data(object_list=object_list,
                                                              subscription=subscription,
                                                              **kwargs)
                    #해당 project에 속해있는 articles, 접속한 유저의 해당 프로젝트의 구독 정보를 돌려준다
    
    
    
    
class ProjectListView(ListView):
    model = Project
    template_name = "projectapp/list.html"
    paginate_by = 25
    context_object_name = 'project_list'