FRONTEND_HOST = 'http://localhost'
PORTAL_NAME = 'MediaCMS'
SECRET_KEY = 'ma!s3^b-cw!f#7s6s0m3*jx77a@riw(7701**(r=ww%w!2+yk2'
POSTGRES_HOST = 'db'
REDIS_LOCATION = "redis://redis:6379/1"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mediacms",
        "HOST": POSTGRES_HOST,
        "PORT": "5432",
        "USER": "mediacms",
        "PASSWORD": "mediacms",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = False

USE_S3_FOR_MEDIA_STORAGE = True
AWS_ACCESS_KEY = 'x'
AWS_SECRET_KEY = 'Y'
S3_BUCKET_NAME = 'Z'


# S3 work plan
# 1. Enter settings that you're using S3 OK
# 2. Enter a migration remote_urls on Media/Encode OK
# 3. add task that puts content to S3, removes local file, sets remote_urls
# 4. API response for orig/encod/hls from S3 --> plays??
# 5. script to migrate existing to S3
