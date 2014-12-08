# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


urlpatterns = i18n_patterns(
    '',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns = [
        url(regex=r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            view=serve,
            kwargs={'document_root': settings.MEDIA_ROOT,
                    'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
