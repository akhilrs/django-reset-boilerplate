from django.conf.urls import include, url
from .authentication import urls as auth_urls

urlpatterns = [
    url(r'^authentication/', include(auth_urls)),
]
