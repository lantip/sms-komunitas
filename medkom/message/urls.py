from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'message.views.messages', name='messages'),
    
    url(r'^(?P<msg_id>\d+)/$', 'message.views.view_message'),
    url(r'^(?P<msg_id>\d+)/decline/$', 'message.views.decline'),
<<<<<<< HEAD
    url(r'^(?P<msg_id>\d+)/spam/$', 'message.views.spam'),
=======
>>>>>>> 0da1a47e3668e247db5727015b137e16e1746573
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
)

