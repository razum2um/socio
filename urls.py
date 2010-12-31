from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex = '^$',
        view  = 'core.views.index',
        name  = 'index'
    ),
    (r'^profiles/', include('profiles.urls')),
    (r'^comments/', include('comments.urls')),
    (r'^', include('blogs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )
