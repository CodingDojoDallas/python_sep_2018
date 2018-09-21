
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.home.urls')),
    url(r'^random/', include('apps.random_word.urls')),
    url(r'^time_display$', include('apps.home.urls'))
]
