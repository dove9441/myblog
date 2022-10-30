from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다


def hello_world(request):
    #return HttpResponse("hello world!") #HttpResponse를 직접 리턴
    return render(request, 'base.html')
#처음 이렇게 만들고 root에서 setting.py에서 템플릿 경로 추가






#여기서 만들고 최초 폴더의 urls.py에서 라우팅


# Create your views here. 
