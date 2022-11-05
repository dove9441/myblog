from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):  #UserCreationForm을 상속받는다
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].disabled = True #이거만 없으면 UserCreationForm과 완전 동일하다