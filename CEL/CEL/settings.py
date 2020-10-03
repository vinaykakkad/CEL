import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '30lfgop^0z)uu^ek)s(g8gm#uvg8!wh+##p=2(_%r@pel%2km#'

DEBUG = True

ALLOWED_HOSTS = '*'

# DEFAULT VARIABLES 
MAXIMUM_SELECTED = 2
MAXIMUM_WINNERS = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',

    # custom apps
    'home',
    'forum',
    'account',
    'my_admin',
    'questions',
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

ROOT_URLCONF = 'CEL.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CEL.wsgi.application'

AUTH_USER_MODEL = 'account.Account'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = "uploads/"

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_PORT = config('EMAIL_PORT')

CKEDITOR_CONFIGS = {
    'default': 
        {'toolbar': 'full',
         'extraPlugins':','.join(
             [
                #  'codesnippet'
                 'youtube'
             ]
         )
            # [
            #     ['CodeSnippet']
            # ], 'extraPlugins':'codesnippet',
        #     {
        #         'name': 'basicstyles',
        #         'groups': ['basicstyles', 'cleanup'],
        #         'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
        #     },
        #     {
        #         'name': 'paragraph',
        #         'groups': ['list', 'indent', 'blocks'],
        #         'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
        #     },
        #     {
        #         'name': 'links',
        #         'items': ['Link', 'Unlink']
        #     },
        #     {
        #         'name': 'insert',
        #         'items': ['Image', 'HorizontalRule', 'Table', 'Iframe', ]
        #     },
        #     {
        #         'name': 'colors',
        #         'items': ['TextColor', 'BGColor']
        #     },
        #     {
        #         'name': 'youtube',
        #         'items': ['Youtube',]
        #     }
        # ],
        # 'height': 400,
        # 'width': '100%',
        # 'allowedContent': True,
        # 'uiColor': '#f0f0f0',
        # 'extraPlugins': 'link,iframe,colorbutton,autogrow,youtube',
        # "extraPlugins":'codesnippet',
        # 'autoGrow_maxHeight': 800,
        # 'autoGrow_minHeight': 400,
        # 'removePlugins': 'resize',
        # 'removeButtons': None,
    },
}