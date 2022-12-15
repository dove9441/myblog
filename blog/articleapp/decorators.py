
from django.http import HttpResponseForbidden
from articleapp.models import *



def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) #해당 pk를 가진 article의 객체들을 가져옴
        if not article.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        