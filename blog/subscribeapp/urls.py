from articleapp.views import *
from django.urls import path
from django.views.generic import TemplateView #django 기본 제공 view이다. 
from subscribeapp.views import SubscriptionView

app_name='subscribeapp'


urlpatterns = [
    path('subscribe/',SubscriptionView.as_view(), name='subscribe')
    
]