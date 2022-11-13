from django.forms import ModelForm
from articleapp.models import *


class ArticleCreationForm(ModelForm): #모델을 form으로 변한
    class Meta:
        model = Article
        fields = ['title','image','content']
        #model, form 만들면 migration 하기 이후 view 만들기