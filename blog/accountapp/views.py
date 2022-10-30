from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다


def hello_world(request):
    #return HttpResponse("hello world!") #HttpResponse를 직접 리턴
    return render(request, 'accountapp/hello_world.html') #/accountapp/hello_world가 아니다. 앞에 /는 꼭 빼야 한다

#처음 이렇게 만들고 root에서 setting.py에서 템플릿 경로 추가
#렌더링할 html경로를 적어주는 것






#여기서 만들고 최초 폴더의 urls.py에서 라우팅


# Create your views here. 
