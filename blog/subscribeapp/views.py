from django.shortcuts import render, get_object_or_404 #shortcuts에서 추가하기
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from subscribeapp.models import Subscription
from django.utils.decorators import method_decorator
from projectapp.models import Project
# Create your views here.

#새로운 내장 Class View RedirectView이다
@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        return reverse_lazy('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})
    
    
    def get(self,request,*args,**kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,project=project)
        
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        
        return super(SubscriptionView, self).get(request, *args, **kwargs)