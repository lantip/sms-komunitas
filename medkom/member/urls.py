from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from member.views import person_list, family_list

urlpatterna = [
    url(r'api/person/', person_list.as_view()),
    url(r'api/family/', family_list.as_view()),
]

urlpatterna = format_suffix_patterns(urlpatterna)

urlpatterns = patterns('',
    url(r'^settings/age/$', 'member.views.settings_age', name='setting_age'),
    url(r'^settings/age/(?P<age_id>\d+)/$', 'member.views.view_age'),
    url(r'^settings/age/(?P<age_id>\d+)/delete/$', 'member.views.delete_age'),
    
    url(r'^settings/social/$', 'member.views.settings_social', name='setting_social'),
    url(r'^settings/social/(?P<sos_id>\d+)/$', 'member.views.view_social'),
    url(r'^settings/social/(?P<sos_id>\d+)/delete/$', 'member.views.delete_social'),


    url(r'^statistics/$', 'member.views.statistics', name='statistics'),
    url(r'^api/bulk/$', 'member.views.receive_json', name='bulk_insert'),
    url(r'^api/send/$', 'member.views.newmessage', name='api_new_message'),
    url(r'^$', 'member.views.home', name='member'),
    url(r'^(?P<member_id>\d+)/$', 'member.views.view_member'),
) + urlpatterna