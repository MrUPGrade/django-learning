from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from basics.views.rapi import router

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url(r'^', include('basics.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^rapi/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
