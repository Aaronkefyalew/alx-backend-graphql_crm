from crm.settings import *  # noqa: F401,F403

# Explicit INSTALLED_APPS entries for naive string-based checkers
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',  # graphene-django
    'django_filters',
    'crm',
]
