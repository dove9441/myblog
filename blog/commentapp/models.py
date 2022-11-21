from django.db import models
from articleapp.models import Article
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment') #Article 객체를 사용할 수 있게 연결
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False) #댓글은 무조건 뭐라도 작성 필요
    created_at = models.DateTimeField(auto_now=True)