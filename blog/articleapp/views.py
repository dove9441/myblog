from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from articleapp.forms import *
from articleapp.decorators import *
from django.views.generic.edit import FormMixin
from commentapp.forms import *


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
    
    
class ArticleDetailView(DetailView, FormMixin): #detailview에서 comment의 form을 같이 사용하기 때문에 다중상속
    model = Article
    template_name = 'articleapp/detail.html'
    context_object_name = 'target_article'
    
    def get_form_class(self):
        if self.request.user.is_authenticated:
            return CommentCreationForm
        else:
            return AnonymousCommentCreationForm
    #form_class = AnonymousCommentCreationForm
    #form_class = CommentCreationForm #다중상속을 통해 가져올 수 있음 물론 import 필요
    
    
    
    
    
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
    template_name = 'articleapp/list.html'
    ordering = ['-created_at']
    paginate_by = 15 #paginate_by는 한 목록에 몇 개의 글을 보여줄지를 결정한다. css grid 사용 시 주의하여 볼 것!
    #오류 해결을 위한 퀴리문 작성
    #er = Article.objects.get(pk="43").title
    #Article.objects.get(pk="43").delete()
    #print(" ############################## 해당 쿼리 : ",er)