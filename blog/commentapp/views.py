from django.shortcuts import render
from commentapp.models import *
from commentapp.forms import *
from django.urls import reverse_lazy
from django.views.generic import * #CreateView, DeleteView

from articleapp.models import Article

from django.utils.decorators import method_decorator
from commentapp.decorators import *
# Create your views here.



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    
    def form_valid(self,form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk']) # input hidden으로 보낸 article_pk
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    
    def get_success_url(self): 
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.article.pk}) #self.object는 comment이다
    
    
    
@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self): 
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.article.pk})

    

# 익명 댓글 Views
class AnonymousCommentCreationForm(CreateView):
    model = AnonymousComment
    form_class = AnonymousCommentCreationForm
    template_name = 'commentapp/anonymouscreate.html' #추후 위의 create.html과 login 상태 확인하여 다르게 표시하는 형태로 통합할 것
    
    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk' : self.object.article.pk })