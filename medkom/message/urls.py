from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from message.views import incoming_list, archive_list

urlpatterna = [
    url(r'api/incoming/', incoming_list.as_view()),
    url(r'api/archive/', archive_list.as_view()),
]

urlpatterna = format_suffix_patterns(urlpatterna)

urlpatterns = patterns('',
    url(r'^$', 'message.views.messages', name='messages'),
    
    url(r'^(?P<msg_id>\d+)/$', 'message.views.view_message'),
    url(r'^(?P<msg_id>\d+)/decline/$', 'message.views.decline'),
    url(r'^(?P<msg_id>\d+)/spam/$', 'message.views.spam'),
    url(r'^(?P<msg_id>\d+)/delete/$', 'message.views.delete'),
    url(r'^(?P<msg_id>\d+)/reply/$', 'message.views.reply'),
    
    url(r'^new/$', 'message.views.new_message', name="new_message"),
    url(r'^new/(?P<no_hp>\d+)/$', 'message.views.new_single_message'),
    
    url(r'^archive/$', 'message.views.archive', name='archive'),
    url(r'^log/$', 'message.views.log', name='log'),
    
    url(r'^settings/broadcast/$', 'message.views.broadcast', name='broadcast'),
    url(r'^settings/broadcast/(?P<b_id>\d+)/$', 'message.views.view_broadcast'),
    url(r'^settings/broadcast/(?P<b_id>\d+)/delete/$',
        'message.views.delete_broadcast'),
) + urlpatterna

