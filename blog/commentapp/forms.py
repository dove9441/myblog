from commentapp.models import *
from django.forms import ModelForm
from django import forms

class CommentCreationForm(ModelForm):
    # WYSIWYG 적용 
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable', #내장 CharField의 여러 속성들을 변경한다. text-left는 부트스트랩 class css이다
                                                          'style' : 'height: auto; text-align: left;'  }))
    class Meta:
        model = Comment
        fields = ['content']
        
        

class AnonymousCommentCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable',
                                                          'style' : 'height:auto; text-align: left;' }))
    
    class Meta:
        model = AnonymousComment
        fields = ['writer', 'password', 'content']
        
        widgets = {
            'writer' : forms.TextInput(
                attrs = {
                    'class' : 'form-control ml-2'
                }
            ),
            
            'password' : forms.TextInput(
                attrs = {
                    'class' : 'form-control ml-2'
                }
            ),
            
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'form-control'
                }
            )
        }
        
            
            
            

#model, form 만들고 migration하기
        