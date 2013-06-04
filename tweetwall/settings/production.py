from common import *

DEBUG = env('DEBUG_APP', False)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = env('EMAIL_HOST', '')

EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')

EMAIL_HOST_USER = env('EMAIL_HOST_USER', '')

EMAIL_PORT = env('EMAIL_PORT', '')

EMAIL_USE_TLS = True

SERVER_EMAIL = EMAIL_HOST_USER
