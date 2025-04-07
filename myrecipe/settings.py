"""
Django settings for myrecipe project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from pathlib import Path
import os
import dj_database_url
from decouple import config,Csv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import environ  # <-- Updated!
from django.core.management.utils import get_random_secret_key

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

# Get the MODE setting (dev or prod)
MODE = env.str('MODE', default='dev')

# SECRET_KEY (keep this secret for production)
SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())


print("MODE:", env.str("MODE"))
print("DB_NAME:", env.str("DB_NAME"))


#Development
if MODE == "dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('DB_NAME', default='recipedata'),
            'USER': env.str('DB_USER', default='postgres'),
            'PASSWORD': env.str('DB_PASSWORD', default='password'),
            'HOST': env.str('DB_HOST', default='localhost'),
            'PORT': env.str('DB_PORT', default='5432'),
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=env.str('DATABASE_URL')
        )
    }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DATABASES = {
    'default': env.db(),  # This uses DATABASE_URL directly
}




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')  # <-- Updated!

# Set ALLOWED_HOSTS based on the environment
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'recipe-nyumbani.fly.dev']
CSRF_TRUSTED_ORIGINS = ['https://fly.io/apps/recipe-nyumbani']



# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'recipeapp',
    'cloudinary',
    'bootstrap4',
    'crispy_forms',
    'crispy_bootstrap4',




]
CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap4"]


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]


ROOT_URLCONF = 'myrecipe.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'myrecipe.wsgi.application'




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Africa/Nairobi'


USE_I18N = True


USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # <-- Updated!
STATIC_URL = 'static/'


STATICFILES_DIRS = [
    BASE_DIR / "static",  # Where your actual static files live
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # <-- Updated!




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



LOGIN_REDIRECT_URL= 'home'
LOGOUT_REDIRECT_URL= 'home'








# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field






DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'







