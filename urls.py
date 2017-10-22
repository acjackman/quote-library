# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.views import defaults as default_views
from django.views.generic import TemplateView

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

from quotelibrary import views

urlpatterns = [
    # add your own patterns here
    url(r'^$', views.home_page, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # User management
    url(r'^users/', include('quotelibrary.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # API URLs
    url(r'^api/v1/', include('api.urls', namespace='v1')),

    # Application URLs
    url(r'authors/', include('authors.urls', namespace='authors')),
    url(r'quotes/', include('quotes.urls', namespace='quotes')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
