from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
# Create your models here.



class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) #탈퇴 시 게시글이 사라지지 않고 게시글 작성자(writer)를 NULL로 변환 #set_NULL이라서 null=True도 해줘야 한다
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True) #Projectapp과 연결
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False) #media/article에 저장된다.
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    