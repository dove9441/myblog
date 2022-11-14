from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from articleapp.forms import *
from articleapp.decorators import *


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    
    def form_valid(self,form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk' : self.object.pk}) #왜 profileapp에서는 reverse_lazy를 썼는데 상관없나? 또 pk=에서 self.object.user.pk가 아닌 자체 pk를 썼을까
    
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articleapp/detail.html'
    context_object_name = 'target_article'
    
    
    
    
    
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'
    context_object_name = 'target_article'
    
    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk' : self.object.pk}) 
    

    
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'
    
    #제발 View 만들면 urls.py에서 만들자
    
    
class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    tamplate_name = 'articleapp/list.html'
    paginate_by = 25 #paginate_by는 한 목록에 몇 개의 글을 보여줄지를 결정한다.