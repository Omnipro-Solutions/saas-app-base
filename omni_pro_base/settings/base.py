from pathlib import Path

from environs import Env
from kombu import Queue as kombuQueue

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    "SECRET_KEY",
    default="django-insecure--fspfc--yg!p^)bi--2brjgyzb^fmu-3bh-#xxmb7gye7(b1-f",
)

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
TIME_ZONE = env.str("TIME_ZONE", default="UTC")
LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en-us")
SITE_ID = 1
USE_I18N = env.bool("USE_I18N", default=True)
USE_TZ = env.bool("USE_TZ", default=True)

THEME_APPS = ["jazzmin"]

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "oauth2_provider",
    "rest_framework",
    "rest_framework.authtoken",
    "auditlog",
    "django_json_widget",
    "django_celery_results",
    "omni_pro_base",
    "omni_pro_oms",
    "rangefilter",
    "django_celery_beat",
    "import_export",
]

INSTALLED_APPS = THEME_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),
}

# Configurar las opciones adicionales para la conexión
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Asegurarte de que el motor sea el correcto
DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "OMS App",
    "site_header": "OMS App",
    "welcome_sign": "Welcome to OMS App",
    "site_brand": "OMS APP",
    "copyright": "© ATM Services All Rights Reserved",
    "login_logo": "vendor/omni/img/logo_login.svg",
    "custom_css": "vendor/omni/css/main.css",
    "custom_js": "vendor/omni/js/main.js",
    "site_logo": "vendor/omni/img/logo.svg",
    "site_icon": "vendor/omni/img/favicon.ico",
    "related_modal_active": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-cube",
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": None,
    "sidebar": "sidebar-light-primary",
    "body_small_text": True,
    "sidebar_nav_compact_style": True,
}

JAZZMIN_SETTINGS["show_ui_builder"] = False

# Application definition
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope",
        "rest_framework.permissions.IsAuthenticated",
    ),
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    "SCOPES": {"read": "Read scope", "write": "Write scope"},
    # Tiempo de expiración para el access token (en segundos)
    "ACCESS_TOKEN_EXPIRE_SECONDS": env.int("OAUTH2_PROVIDER__TOKEN_EXPIRE_SECONDS", 60 * 60),  # 1 hora
    # Tiempo de expiración para el ID token (en segundos)
    "ID_TOKEN_EXPIRE_SECONDS": env.int("OAUTH2_PROVIDER__TOKEN_EXPIRE_SECONDS", 60 * 60),  # 1 hora
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

AUTH_USER_MODEL = "omni_pro_base.User"
LOGIN_REDIRECT_URL = "/admin/"

ADMIN_URL = env.str("ADMIN_URL", default="admin/")
ADMIN_LOGIN = env.str("ADMIN_LOGIN", default="oms@omni.pro")
ADMIN_PASSWORD = env.str(
    "ADMIN_PASSWORD",
    default="argon2$argon2id$v=19$m=102400,t=2,p=8$WVlMYVg1ZkJhMDRyV1hkb2hhb1BkdA$xsgpDV8dbFLBKM83JkTxJDCYCk30pbMo35KzwUXo848",
)
ADMIN_USERNAME = env.str("ADMIN_USERNAME", default=ADMIN_LOGIN)
ADMIN_FIRST_NAME = env.str("ADMIN_FIRST_NAME", default="OMS")
ADMIN_LAST_NAME = env.str("ADMIN_LAST_NAME", default="OMNI")
AUTH_BASE_URL = env.str("AUTH_BASE_URL", default="http://localhost:8000")
AUTH_APP_SERVICE_URL = env.str("AUTH_APP_SERVICE_URL", default=f"{AUTH_BASE_URL}/auth/users/login/")

AUTHENTICATION_BACKENDS = [
    "omni_pro_base.backends.SettingsBackend",
    "omni_pro_base.backends.AppUserBackend",
    "django.contrib.auth.backends.ModelBackend",
]

ADMINS = [("Author", "OMNI.PRO")]
MANAGERS = ADMINS

# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "SAMEORIGIN"

# Email
EMAIL_BACKEND = env.str("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = env.str("STATIC_URL", default="static/")
# STATIC_ROOT = env.str("STATIC_ROOT", default=str(BASE_DIR / "staticfiles/"))
# STATICFILES_FINDERS = [
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# ]

STATIC_URL = env.str("STATIC_URL", default="static/")
STATIC_ROOT = env.str("STATIC_ROOT", default="/app/staticfiles")

MEDIA_URL = env.str("MEDIA_URL", default="media/")
MEDIA_ROOT = env.str("MEDIA_ROOT", default=str(BASE_DIR / "media/"))

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CONFIGURATION CELERY
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
else:
    CELERY_TIMEZONE = "UTC"

CELERY_NAME_APP_DJANGO = env.str("CELERY_NAME_APP_DJANGO", default="django_app")
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", default="redis://127.0.0.1:6379/0")
# RESULT_BACKEND = env.str("RESULT_BACKEND", default=CELERY_BROKER_URL)
# RESULT_BACKEND = "django-db"

# QUEUE
# Celery settings
QUEUE_CRITICAL = f"{CELERY_NAME_APP_DJANGO}.critical"
QUEUE_HIGH = f"{CELERY_NAME_APP_DJANGO}.high"
QUEUE_MEDIUM = f"{CELERY_NAME_APP_DJANGO}.medium"
QUEUE_LOW = f"{CELERY_NAME_APP_DJANGO}.low"
QUEUE_VERY_LOW = f"{CELERY_NAME_APP_DJANGO}.very_low"

CELERY_NAME_QUEUE = QUEUE_MEDIUM
CELERY_HIGH_PRIORITY_QUEUE = QUEUE_MEDIUM

CELERY_TASK_DEFAULT_QUEUE = QUEUE_LOW
CELERY_TASK_DEFAULT_ROUTING_KEY = QUEUE_LOW

CELERY_TASK_QUEUES = [
    kombuQueue(
        name=QUEUE_CRITICAL,
        exchange=QUEUE_CRITICAL,
        routing_key=QUEUE_CRITICAL,
    ),
    kombuQueue(
        name=QUEUE_HIGH,
        exchange=QUEUE_HIGH,
        routing_key=QUEUE_HIGH,
    ),
    kombuQueue(
        name=QUEUE_MEDIUM,
        exchange=QUEUE_MEDIUM,
        routing_key=QUEUE_MEDIUM,
    ),
    kombuQueue(
        name=QUEUE_LOW,
        exchange=QUEUE_LOW,
        routing_key=QUEUE_LOW,
    ),
    kombuQueue(
        name=QUEUE_VERY_LOW,
        exchange=QUEUE_VERY_LOW,
        routing_key=QUEUE_VERY_LOW,
    ),
]
CELERY_TASK_ROUTES = {
    f"{CELERY_NAME_APP_DJANGO}.tasks.critical_*": {
        "queue": QUEUE_CRITICAL,
        "routing_key": QUEUE_CRITICAL,
    },
    f"{CELERY_NAME_APP_DJANGO}.tasks.high_*": {
        "queue": QUEUE_HIGH,
        "routing_key": QUEUE_HIGH,
    },
    f"{CELERY_NAME_APP_DJANGO}.tasks.medium_*": {
        "queue": QUEUE_MEDIUM,
        "routing_key": QUEUE_MEDIUM,
    },
    f"{CELERY_NAME_APP_DJANGO}.tasks.low_*": {
        "queue": QUEUE_LOW,
        "routing_key": QUEUE_LOW,
    },
    f"{CELERY_NAME_APP_DJANGO}.tasks.very_low_*": {
        "queue": QUEUE_VERY_LOW,
        "routing_key": QUEUE_VERY_LOW,
    },
}

CELERY_WORKER_PREFETCH_MULTIPLIER = 1

ACCEPT_CONTENT = ["json"]
RESULT_SERIALIZER = "json"
TASK_SERIALIZER = "json"

RESULT_PERSISTENT = True
CELERY_TASK_PERSISTENT = True
broker_connection_retry_on_startup = True

CELERY_MAX_RETRIES = env.int("CELERY_MAX_RETRIES", default=3)
CELERY_SECONDS_TIME_TO_RETRY = env.int("CELERY_SECONDS_TIME_TO_RETRY", default=30)

# CONFIGURATION CELERY RESULTS
CELERY_RESULT_EXTENDED = True
CELERY_CACHE_BACKEND = "django-cache"
CELERY_RESULT_BACKEND = "django-db"

ASYNC_TIMEOUT = env.int("ASYNC_TIMEOUT", default=30)  # tiempo en segundos

# CONFIGURATION CELERY BEAT
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# CONFIGURATION LOGGING
LOGGING_LEVEL = env.str("LOGGING_LEVEL", default="INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] - [{asctime}]: {name} in line {lineno} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        # "file": {  # Handler for logging to a file
        #     "class": "logging.FileHandler",
        #     "filename": "debug.log",
        #     "formatter": "verbose",
        # },
    },
    "root": {
        "handlers": ["console"],
        "level": LOGGING_LEVEL,
    },
}

# CONFIGURATION EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_SSL = True

EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="smtp_user")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="smtp_password")
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="smtp_email")
