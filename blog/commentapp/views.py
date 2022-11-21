from django.shortcuts import render
from commentapp.models import *
from commentapp.forms import *
from django.urls import reverse_lazy
from django.views.generic import *

from articleapp.models import Article

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