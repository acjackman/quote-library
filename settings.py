# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-devsync',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'markdown_deux',  # markdown
    'rest_framework',  # REST API
    'rest_framework.authtoken',  # Token based authentication
    'django_filters',  # Filtering
]

LOCAL_APPS = [
    'quotelibrary.users.apps.UsersConfig',
    'authors',
    'quotes',
    'api',
]

INSTALLED_APPS.extend(THIRD_PARTY_APPS + LOCAL_APPS)

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
# AUTHENTICATION_BACKENDS.extend([
#     'allauth.account.auth_backends.AuthenticationBackend',
# ])

# # Some really nice defaults
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# ACCOUNT_ALLOW_REGISTRATION = True
# ACCOUNT_ADAPTER = 'quotelibrary.users.adapters.AccountAdapter'
# SOCIALACCOUNT_ADAPTER = 'quotelibrary.users.adapters.SocialAccountAdapter'

# # Custom user app defaults
# # Select the correct user model
# # AUTH_USER_MODEL = 'users.User'
# LOGIN_REDIRECT_URL = 'users:redirect'
# LOGIN_URL = 'account_login'

# # SLUGLIFIER
# AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# REST Framework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'PAGE_SIZE': 100,
    'DEFAULT_PERMISSION_CLASSES': (
        'api.permissions.IsAdminOrReadOnly',
    )
}

# Debugging
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.extend(["debug_toolbar"])

    def _show_toolbar(request):
        return True

    MIDDLEWARE_CLASSES.insert(
        MIDDLEWARE_CLASSES.index("django.middleware.gzip.GZipMiddleware") + 1,
        "debug_toolbar.middleware.DebugToolbarMiddleware"
        )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': _show_toolbar,
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'incremental': True,
        'root': {
            'level': 'DEBUG',
        },
    }
