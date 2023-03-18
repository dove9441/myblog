from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from projectapp.forms import *
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article
from subscribeapp.models import Subscription
from django.utils.decorators import method_decorator
from projectapp.decorators import project_ownership_required

# Create your views here.
@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    
    
    def get_success_url(self):
        return reverse_lazy('projectapp:detail', kwargs={'pk' : self.object.pk})
    
#DeleteView가 작동하지 않았던 이유가 writer를 만들어놓고 form_valid로 지정을 안 해줘서 그런 것이었다.
    def form_valid(self,form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)
    
    
class ProjectDetailView(DetailView, MultipleObjectMixin): #믹스인 사용
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    
    def get_context_data(self, **kwargs): #템플릿에게 데이터를 전달하기 위해 오버라이딩
        project = self.object
        user = self.request.user
        
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object()) #해당 project에 속해있는 articles를 가져오는 건데 이해는 잘 안 된다.
        ordered_list = Article.objects.order_by('-created_at')
        return super(ProjectDetailView,self).get_context_data(object_list=ordered_list,
                                                              subscription=subscription,
                                                              **kwargs)
                    #해당 project에 속해있는 articles, 접속한 유저의 해당 프로젝트의 구독 정보를 돌려준다
    
    
    
    
class ProjectListView(ListView):
    model = Project
    template_name = "projectapp/list.html"
    paginate_by = 25
    context_object_name = 'project_list'


@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projectapp/delete.html'
    context_object_name = "target_project"
    success_url = reverse_lazy("projectapp:list")
    
    
    

@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projectapp/update.html'
    form_class = ProjectCreationForm
    context_object_name = 'target_project'
    
    def get_success_url(self):
        return reverse_lazy('projectapp:detail', kwargs={'pk' : self.object.pk})
        
        
        
        
#View 만들면 제발 urls.py에 추가하자.............
