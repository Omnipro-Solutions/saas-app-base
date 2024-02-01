DEBUG = True

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "OMS Magento",
    "site_header": "OMS Magento",
    "welcome_sign": "Welcome to OMS Magento App",
    "site_brand": "OMS MAGENTO APP",
    "copyright": "Omni Pro SAS",
    # "login_logo": "/img/logo_login.svg",
    # "custom_css": "/css/main.css",
    # "custom_js": "/js/main.js",
    "site_logo": "/img/logo.svg",
    "site_icon": "/img/favicon.ico",
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
