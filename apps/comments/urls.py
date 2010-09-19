from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('comments.views',
    url(
        regex = '^(?P<item_id>\d+)/add/$',
        view  = 'new',
        name  = 'new_comment'
    ),
)

