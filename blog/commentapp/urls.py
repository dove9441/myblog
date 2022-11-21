from django.urls import path, include
from commentapp.views import *

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]