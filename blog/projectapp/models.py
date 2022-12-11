from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return f'{self.pk} : {self.title}' #article create의 project select에서 표시되는 이름을 pk : title 로 변경