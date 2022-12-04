from django.urls import include, path
from projectapp.views import *


app_name = 'projectapp'

urlpatterns=[
    path('list/', ProjectListView.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('create/', ProjectCreateView.as_view(), name='create'),
]
    