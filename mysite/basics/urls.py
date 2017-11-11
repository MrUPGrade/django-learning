from django.conf.urls import url

import basics.views.auth as auth_views
import basics.views.contact as contact_views
import basics.views.other as other_views
import basics.views.tags as tags_views
from .views import api as api_views

app_name = 'basics'

urlpatterns = [
    url(r'^$', other_views.index, name='index'),

    url(r'^vuetest/$', other_views.vuetest, name='vuetest'),

    url(r'^contact/all/$', contact_views.all_contacts, name='contact-all'),
    url(r'^contact/add/$', contact_views.AddContactView.as_view(), name='contact-add'),
    url(r'^contact/details/(?P<pk>[-\w]+)/$', contact_views.ContactDetailView.as_view(),
        name='contact-details'),

    url(r'^tags/$', tags_views.TagsView.as_view(), name='tags'),
    url(r'^tags/add/$', tags_views.AddTagsView.as_view(), name='tags-add'),

    url(r'^auth/login/$', auth_views.MyLoginView.as_view(), name='login'),
    url(r'^auth/logout/$', auth_views.logout_view, name='logout'),

    # API
    url(r'^api/hello', api_views.hello_world, name='api_hello'),
]
