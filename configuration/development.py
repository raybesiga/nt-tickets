DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_URL="http://localhost:8000"

ACTUALLY_SEND_MAIL = False

PUBLIC_CATEGORIES = ['theatre','uncut']

ACTUALLY_SEND_MAIL = True
DO_CHIMP = False

AWS_STORAGE_BUCKET_NAME = "nt-tickets-dev"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_LOCATION = 'static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

AWS_S3_SECURE_URLS = False    # Use HTTP instead of HTTPS
AWS_QUERYSTRING_AUTH = False    # Remove auth querystrings from the query

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

ACTUALLY_SEND_MAIL = False
DO_CHIMP = False
