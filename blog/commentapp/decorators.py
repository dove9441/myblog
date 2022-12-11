
from django.http import HttpResponseForbidden
from articleapp.models import *
from commentapp.models import *


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk']) #접속중인 사람의 pk를 가져옴
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        