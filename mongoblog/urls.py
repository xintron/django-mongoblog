from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'mongoblog.views.entry_list', name = 'blog_entry_list'),

    url(r'^(?P<slug>[-\w]+)/$', 'mongoblog.views.entry_detail', name = 'blog_entry_detail'),
)
