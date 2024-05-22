""" Production settings """

from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*.omni.pro"])
ALLOWED_CIDR_NETS = env.list("ALLOWED_CIDR_NETS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

DJA = len(THEME_APPS + DJANGO_APPS)
INSTALLED_APPS.insert(DJA, "corsheaders")

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
MIDDLEWARE.insert(4, "corsheaders.middleware.CorsMiddleware")

# whitenoise settings
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
STATIC_HOST = env.str("DJANGO_STATIC_HOST", default="")
STATIC_URL = STATIC_HOST + "/static/"

# Cache
# TODO: falta por implementar
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": env.list("REDIS_URL", default=["redis://127.0.0.1:6379"]),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "IGNORE_EXCEPTIONS": True,
#         },
#     }
# }
