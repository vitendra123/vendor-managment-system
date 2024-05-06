# Imports
import os
import dotenv
from pathlib import Path


# Load environment variables
dotenv.load_dotenv()


# Set the base directory for the project
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Set the base path for the apps
APPS_DIR = BASE_DIR / "apps"


# Set the debug status of the project
DEBUG = eval(os.environ.get("DEBUG", False))


# Set the secret key for the project
SECRET_KEY = os.environ.get("SECRET_KEY")


# Set the CORS origin whitelist
CORS_ALLOWED_ORIGINS = ["https://*"]


# Allowed hosts
ALLOWED_HOSTS = ["*"]


# Internationalization
TIME_ZONE = "Asia/Kolkata"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_TZ = True


# Default auto field for django models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Root URL configuration file
ROOT_URLCONF = "config.urls"


# WSGI application
WSGI_APPLICATION = "config.wsgi.app"


# Set the auth user model
AUTH_USER_MODEL = "core.CustomUser"


# Django apps
DJANGO_APPS = [
    "jazzmin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]

# Third party apps
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
]


# Local apps
LOCAL_APPS = ["apps.core", "apps.vendors", "apps.purchase_orders", "apps.performance"]


# Combine all apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Default database settings with sqlite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database" / "db.sqlite3",
    }
}


# Django authentication settings
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]


# Password hashers setting
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# Auth password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Static files settings
STATIC_ROOT = BASE_DIR / "staticfiles" / "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Django templates settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [APPS_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Set directory for fixtures
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)


# Security settings
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"


# Admin settings
ADMIN_URL = "admin/"
ADMINS = [("""Rohit Vilas Ingole""", "rohit.vilas.ingole@gmail.com")]
MANAGERS = ADMINS


# Rest framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "apps.core.authentication.QueryParameterTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}
