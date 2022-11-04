from django.db import models

# Create your models here.
# 모덷 클래스를 작성하고 나서 python manage.py makemigrations을 해야 blog/migrations에 새로운 .py가 생긴다.
# 이후 python manage.py migrate를 실행한다. 그러면 자동으로 db와 연동이 된다.
# blog/migrations 안의 파일은 삭제하는 다른 방법이 있으니 임의로 삭제하지 말자




class HelloWorld(models.Model): #HelloWorld 객체는 text 멤버변수를 가지고 있다.
    text = models.CharField(max_length=255, null=False)