from django.conf.urls import patterns, url

urlpatterns = patterns(
 url(r'^show/(?P<notification_id>\d+)/$' , 'show_notificaton'),
 url(r'^delete/(?P<notification_id>\d+)/$' , 'delete_notificaton'),
             )