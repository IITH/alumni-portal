from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('portalapp.urls', namespace='portalapp')),

    url(r'^auth/', include('google-auth.urls', namespace='google-auth')),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url('', include('django.contrib.auth.urls', namespace='auth')),
)
