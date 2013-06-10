# Django settings for yapebuy project.
#encoding=utf-8
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Importamos Path de unipath(pip install unipath).
# Luego retrocedemos 2 directorios.
from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

ADMINS = (
    ('Qaysen', 'admin@qaysen.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sitio.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Lima'

LANGUAGE_CODE = 'es-PE'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Agregamos el nombre de la carpeta media.
MEDIA_ROOT = RUTA_PROYECTO.child("media")

# Tenemos que poner la direccion completa para que cargue los archivos.
MEDIA_URL = 'http://localhost:8000/media/'

# Aqui deberia ir vacio.
STATIC_ROOT = ''

STATIC_URL = '/static/'

# Agregamos el nombre de la carpeta estatico.
STATICFILES_DIRS = (
    RUTA_PROYECTO.child("static"),  # ruta de archivos estaticos css y js
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '2h$90la2^d+u96mg4494ibr$k2)nrnlkodpq*(wci!q72huq6x'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'SitioQaysen.urls'

WSGI_APPLICATION = 'SitioQaysen.wsgi.application'

# Agregamos el nombre de la carpeta plantillas.
TEMPLATE_DIRS = (
    RUTA_PROYECTO.child("plantillas"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'principal',
    
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='qaysen.sac@gmail.com'
EMAIL_HOST_PASSWORD='qaysenedwin'
EMAIL_USE_TLS=True