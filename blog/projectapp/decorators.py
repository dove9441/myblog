
from django.http import HttpResponseForbidden
from projectapp.models import *



def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk']) #해당 pk를 가진 project의 객체들을 가져옴
        if not project.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        