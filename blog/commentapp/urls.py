from django.urls import path, include
from commentapp.views import *

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
    path('anonymouscreate/', AnonymousCommentCreateView.as_view(), name='anonymouscreate'),
    path('anonymousdelete/<int:pk>', AnonymousCommentDeleteView.as_view(), name='anonymousdelete'),
]