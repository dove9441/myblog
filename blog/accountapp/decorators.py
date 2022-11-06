from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk']) #접속중인 사람의 pk를 가져옴
        if not user == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        