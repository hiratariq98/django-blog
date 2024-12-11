import os
import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = 'KJQs22SsqyON2pg4jGyep0J52sWxv98l'
ALLOWED_HOSTS = ["*"]

MIDDLEWARE = ("whitenoise.middleware.WhiteNoiseMiddleware" * MIDDLEWARE,)
