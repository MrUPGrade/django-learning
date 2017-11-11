from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import urls as  drf_urls

from basics.views.rapi import router
from basics import urls as basics_urls

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(basics_urls)),

    url(r'^admin/', admin.site.urls),

    url(r'^rapi/', include(router.urls)),
    url(r'^api-auth/', include(drf_urls)),
    url(r'^schema/$', schema_view),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
