from django.conf.urls import url, patterns

urlpatterns = patterns('taggit_autocomplete.views',
    url(r'^list$', 'list_tags', name='taggit_autocomplete-list'),
)
