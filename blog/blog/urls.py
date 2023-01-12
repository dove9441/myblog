"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse #include 추가
#미디어 라우팅을 위한 import 
from django.conf.urls.static import static #static 안의 static이다
from django.conf import settings
from articleapp.views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    
    path('admin/', admin.site.urls),
    path('accounts/',include('accountapp.urls')), # ,까지 
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribes/', include('subscribeapp.urls')),
    #소셜 로그인 앱
    path('socialauth/', include('socialauth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")), #이건 꼭 최상위 urls.py에 써줘야 한다.
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
