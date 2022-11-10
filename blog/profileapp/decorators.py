from django.http import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) #접속중인 사람의 pk를 가져옴
        if not profile.user == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
        
    return decorated
        