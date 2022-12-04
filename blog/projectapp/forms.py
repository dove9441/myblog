from django.forms import ModelForm
from projectapp.models import *

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image','title','description'] #순서대로 위쪽부터 나옴
        #model, form 만들면 migration 하기 이후 view 만들기