
from django.http import HttpResponseForbidden
from articleapp.models import *



def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) #접속중인 사람의 pk를 가져옴
        if not article.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        