from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


GOOGLE_API_SETTINGS = BASE_DIR / 'conf/bionic-path-363401-5b625865ca8d.json'
KEY = '1CR87pQz_OR6ljfD_S-yqKLG7oXOwy75RQ-5o4gmPcfw'

# CRONJOBS = [
#     ('*/1 * * * *', 'parse_doc.cron.my_scheduled_job','>>/tmp/test.log')
# ]
CRONJOBS = [
    ('*/1 * * * *', 'parse_doc.cron.my_scheduled_job')
]
SECRET_KEY = 'django-insecure-!g2v03t684)(cq+e2z4=zax)np3+^-6u%&w6%utxvb)9rpmigf'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'googlecharts',
    'parse_doc.apps.ParseDocConfig',
    'singlpage.apps.SinglpageConfig'
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
ROOT_URLCONF = 'test_hh.urls'
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
WSGI_APPLICATION = 'test_hh.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'data',
         'USER': 'flatr',
         'PASSWORD': 'flatr',
         'HOST': 'db',
         'PORT': '5432',
     }
}
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
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
