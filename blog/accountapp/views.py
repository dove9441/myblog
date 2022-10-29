from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다


def hello_world(request):
    return HttpResponse("hello world!")
#여기서 만들고 최초 폴더의 urls.py에서 라우팅


# Create your views here. 
