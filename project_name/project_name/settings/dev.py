# Fetch our common settings
from .common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT_DIR, 'run', 'dev.sqlite3'),
    }
}

# ##### APPLICATION CONFIGURATION #########################
THIRD_PARTY_APPS = (

)

LOCAL_APPS = (
    'api.v01.authentication',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
