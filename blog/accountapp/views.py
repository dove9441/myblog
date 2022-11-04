from django.shortcuts import render
from django.http import HttpResponse #추가해야 한다


# 모델도 import해야 한다.
from accountapp.models import HelloWorld


# Create your views here. 

def hello_world(request):
    #return HttpResponse("hello world!") #HttpResponse를 직접 리턴
    #form의 method 값 get/post 따라서 요청을 나눈다
    if request.method=="POST":
        temp = request.POST.get('hello_world_input') #request의 post 요청 (하지만 대문자로 써야 한다)에서  input 태그의 name속성값이 hello_world_input인 것의 데이터를 가져와라
        
        
        #DB에 저장하기 
        new_hello_world = HelloWorld() #객체 생성
        new_hello_world.text = temp
        new_hello_world.save()
        
        
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world}) #/accountapp/hello_world가 아니다. 앞에 /는 꼭 빼야 한다 context는 보내줄 데이터다
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': "GET_METHOD!"})

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#처음 이렇게 만들고 root에서 setting.py에서 템플릿 경로 추가
#렌더링할 html경로를 적어주는 것
#여기서 만들고 최초 폴더의 urls.py에서 라우팅



