from django.forms import ModelForm #models.py에서 만든 모델을 form으로 변환해주는 기능을 한다
from profileapp.models import *

class ProfileCreationForm(ModelForm): #클래스의 인자는 상속을 의미하는 것 기억
    class Meta:
        model = Profile #내부 클래스 Meta는 고정, 여기서 model을 받아온다
        field = ['image', 'nickname', 'message']	#model과 field, Meta는 고정 형식이다. form은 말 그대로 html의 form이다
        
    