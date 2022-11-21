from commentapp.models import *
from django.forms import ModelForm

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        #model, form 만들고 migration하기