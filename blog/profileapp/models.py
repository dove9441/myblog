from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") 
    #profile과 user객체를 연결하는 내장 함수 on_delete = cascade는 user객체가 사라질 때(탈퇴) profile도 사라지는 것
    #related_name이란 request.user.profile처럼 연결할 수 있게 하는 것
    
    image = models.ImageField(upload_to='profile/', null=True) #프로필 사진 필드. setting.py에서 정의한 media/에 profile폴더가 새로 만들어진다. null은 이미지를 안 올려도 된다는 뜻 
    nickname = models.CharField(max_length=20, unique=True, null=True) #닉네임 필드
    message = models.CharField(max_length=100, null=True) #간단한 소개 필드
    
    #모델을 만들었으면 python manage.py makemigrations 이후 python manage.py migrate를 해줘야 db와 연동이 된다.
    #이후 View를 만들면 된다
    
    


    