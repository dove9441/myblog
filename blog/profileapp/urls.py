from profileapp.views import *
from django.urls import path

app_name='profileapp'


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
        path('list/', ProfileListView.as_view(), name='list'),

]