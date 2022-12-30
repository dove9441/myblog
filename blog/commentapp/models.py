from django.db import models
from articleapp.models import Article
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='comment') #Article 객체를 사용할 수 있게 연결, 글 삭제 시 댓글 db도 삭제되개.
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False) #댓글은 무조건 뭐라도 작성 필요
    created_at = models.DateTimeField(auto_now=True)
    

    
#익명 댓글 기능 작성하기 related_name은 foreignKey를 사용한 곳애만 사용해야 한다.
class AnonymousComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, related_name='anonymouscomment')
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=12, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=False)
    
#model, form 만들고 migrate하기 