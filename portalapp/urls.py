from django.conf.urls import patterns, url
from portalapp import views
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns(
    '', 
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.view_userinfo, name='view_userinfo'),
    url(r'^profile/create$', views.create_userinfo, name='create_userinfo'),
    url(r'^profile/update/(?P<pk>\d+)$', views.UserInfoUpdate.as_view(success_url=reverse_lazy('portalapp:view_userinfo')), name='update_userinfo'),

)
