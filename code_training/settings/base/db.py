import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'test_db'),
        'USER': os.environ.get('DB_USER', 'test_user'),
        'PASSWORD': os.environ.get('DB_PASS', 'test_password'),
        'PORT': os.environ.get('DB_PORT', 5432),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'CONN_MAX_AGE': 900
    },
}
