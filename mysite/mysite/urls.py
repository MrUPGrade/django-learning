from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from basics.views.rapi import router

urlpatterns = [
    url(r'^', include('basics.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^rapi/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
