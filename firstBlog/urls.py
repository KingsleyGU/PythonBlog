from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'blog.views.home', name='home'),
     url(r'^hello/$', 'blog.views.hello'),
     url(r'^create/$', 'blog.views.create'),
     url(r'^list/$', 'blog.views.list'),
     url(r'^upload_file/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT+"/upload_file/"}),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.PUBLIC_ROOT}),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
