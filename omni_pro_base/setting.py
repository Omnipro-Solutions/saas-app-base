from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="django-insecure--fspfc--yg!p^)bi--2brjgyzb^fmu-3bh-#xxmb7gye7(b1-f")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
ALLOWED_CIDR_NETS = env.list("ALLOWED_CIDR_NETS", default=["127.0.0.0/21"])

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["http://localhost"])

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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
    "SCOPES": {"read": "Read scope", "write": "Write scope"}
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

AUTH_USER_MODEL = "omni_pro_base.User"

ADMIN_URL = env.str("ADMIN_URL", default="admin/")
ADMIN_LOGIN = env.str("ADMIN_LOGIN", default="oms@omni.pro")
ADMIN_PASSWORD = env.str(
    "ADMIN_PASSWORD", default="pbkdf2_sha256$720000$pNo5LfaIsB1mmcKNwdZFfI$U418YPNlY9dMVKrObnP5QBopxLVRGt6BlKxaFp68YGE="
)
ADMIN_USERNAME = env.str("ADMIN_USERNAME", default=ADMIN_LOGIN)
ADMIN_FIRST_NAME = env.str("ADMIN_FIRST_NAME", default="OMS")
ADMIN_LAST_NAME = env.str("ADMIN_LAST_NAME", default="OMNI")
AUTH_APP_SERVICE_URL = env.str("AUTH_APP_SERVICE_URL", default="http://localhost:8000/users/login/")

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
X_FRAME_OPTIONS = "DENY"

# Email
EMAIL_BACKEND = env.str("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en-us")

TIME_ZONE = env.str("TIME_ZONE", default="UTC")

USE_I18N = env.bool("USE_I18N", default=True)

USE_TZ = env.bool("USE_TZ", default=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = env.str("STATIC_URL", default="static/")
STATIC_ROOT = env.str("STATIC_ROOT", default=str(BASE_DIR / "staticfiles/"))
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = env.str("MEDIA_URL", default="media/")
MEDIA_ROOT = env.str("MEDIA_ROOT", default=str(BASE_DIR / "media/"))

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
