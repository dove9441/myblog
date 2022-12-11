
from django.http import HttpResponseForbidden
from projectapp.models import *



def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk']) #접속중인 사람의 pk를 가져옴
        if not project.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        