from django.forms import ModelForm
from articleapp.models import *
from django import forms
from projectapp.models import Project


class ArticleCreationForm(ModelForm): #모델을 form으로 변한
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable', #내장 CharField의 여러 속성들을 변경한다. text-left는 부트스트랩 class css이다
                                                          'style' : 'height: auto; text-align: left;'  }))
    
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False) #project 필수 지정 해제
    class Meta:
        model = Article
        fields = ['title','image','project', 'content'] #순서에 따라 위부터 나타난다.  어떻게 이렇게 바로 설정할 수 있게 되는 거지?
        #model, form 만들면 migration 하기 이후 view 만들기
        #model, form 수정돼도 migration 하기