from .base import *


SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)

X_FRAME_OPTIONS = env('X_FRAME_OPTIONS', default="SAMEORIGIN")

if env.bool("APPLY_EXTRA_SECURITY_SETTINGS", default=False):
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 86400
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True