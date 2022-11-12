from profileapp.views import *
from django.urls import path
from django.views.generic import TemplateView #django 기본 제공 view이다. 

app_name='articleapp'


urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]