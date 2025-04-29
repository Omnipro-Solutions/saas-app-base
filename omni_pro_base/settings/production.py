""" Production settings """

from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*.omni.pro"])
ALLOWED_CIDR_NETS = env.list("ALLOWED_CIDR_NETS", default=[])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

DJA = len(THEME_APPS + DJANGO_APPS)
INSTALLED_APPS.insert(DJA, "corsheaders")

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
MIDDLEWARE.insert(4, "corsheaders.middleware.CorsMiddleware")
MIDDLEWARE.insert(5, "django.middleware.common.CommonMiddleware")

CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=True)

# whitenoise settings
# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# STATIC_HOST = env.str("DJANGO_STATIC_HOST", default="")
# STATIC_URL = STATIC_HOST + "/static/"

# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"

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
