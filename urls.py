from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex = '^$',
        view  = 'core.views.post.index',
        name  = 'index'
    ),
    (r'^profiles/', include('profiles.urls')),
    (r'^comments/', include('comments.urls')),
    (r'^', include('core.urls')),
    # Example:
    # (r'^socio/', include('socio.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

