"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path
from django.urls import reverse, reverse_lazy
#secret key 보호용
import environ


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# environ 사용
env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

SECRET_KEY = env('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp', #여기서 startapp으로 추가한 앱을 추가해야 한다. 마지막 ,도.
    'bootstrap4', #부트스트랩 설치 후 적기
    'profileapp',  ##python manage.py startapp "앱 이름" 생성 후 적기
    'articleapp', #이후 urls.py에서 url 설정하기
    'commentapp',
    'projectapp',
    'subscribeapp',
    'tinymce', #tinymce 사용
    'socialauth', #이것과 아래 1개는 소셜 로그인을 위한 앱 #https://morioh.com/p/3180f4e88887 참고
    'social_django',
    'sslserver', #authcanceled 오류가 ssl서버를 사용하지 않아서 그런 건가??
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #여기서 템플릿의 경로를 추가 base.dir은 앞에 정의되어 있다
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 소셜 로그인 시 사용자 정보를 추가로 가져오기 위한 추가
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]







WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


#python manage.py collectstatic으로 static 파일들을 모을 수 있음. 아래 경로가 그 파일들이 모이는 경로임. css 등 잘 변경하지 않는 것을 static으로 변경하기 위함.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [ 
    os.path.join (BASE_DIR, 'static'),   #blog/static을 의미한다 (콤마 필수)
                   ] 


LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login') #로그아웃 시 윗줄의 LOGIN_REDIRECT_URL로 이동. 여기서 또 hello_world로 이동한다. 결국 로그인, 로그아웃 시 모두 hello_world로 이동.


#소셜 로그인을 위한 추가
#LOGIN_URL = 'login'
#LOGOUT_URL = 'logout'

#이거 추가하니까 됐다 !!!!
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True 


SOCIAL_AUTH_FACEBOOK_KEY = "1547573535754510"    # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = "4107a848e8e4fa99f66c73c59c0b7c79"  # App Secret

SOCIAL_AUTH_INSTAGRAM_KEY = "444554391100080"
SOCIAL_AUTH_INSTAGRAM_SECRET = "48f1ff92d6080dcfa0c3c5e56086ac65"


SOCIAL_AUTH_FACEBOOK_API_VERSION = '15.0'


SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}



AUTHENTICATION_BACKENDS = [
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


SOCIAL_AUTH_URL_NAMESPACE = 'social'
# 여기까지 소셜 로그인을 위한 추가




MEDIA_URL = '/media/' #주소창에서 접근하는 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #파이썬 파일에서 접근하는 경로


TINYMCE_JS_URL = "https://cdn.tiny.cloud/1/gxr8kvj7d7ud5xjy8k4tqvbjz1mlfwj09f6ol6n9s8x0gggv/tinymce/6/tinymce.min.js"
TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

#처음 이렇게 만들고(앱 내부의 views.py) root에서 setting.py에서 템플릿 경로 추가
#렌더링할 html경로를 적어주는 것
#여기서 만들고 최초 폴더의 urls.py에서 라우팅

# 1. 앱 만들기 (python manage.py startapp '앱 이름')
# 2. settings.py에 앱 추가
# 3. urls.py(프로젝트 폴더)에서 경로 지정
# 4. 앱 내부에 urls.py 만들기
# 5. 모델 만들기
# 6. form 만들기
# 7. python manage.py makemigrations 이후 python manage.py migrate를 해줘야 db와 연동이 된다.
# 8. View 만들기

# !! View 만드는 순서 : 
# 1. View.py에 class나 function 만들기 (template_name 등 추가)
# 2. urls.py에 path 추가하기
# 3. template 폴더에서 html 파일 작성하기



