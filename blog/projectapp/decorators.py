
from django.http import HttpResponseForbidden
from projectapp.models import *



def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk']) #해당 pk를 가진 project의 객체들을 가져옴
        #project writer가 아마 개발 과정으로 인해 설정되어있지 않아서 none으로 나타나서 제대로 작동하지 않을 수도 있음
        #print("project.writer : ", project.writer, ", request : ", request.user)
        if not project.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
        
    return decorated
        