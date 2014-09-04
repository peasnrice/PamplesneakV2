from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pamplesneak.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'accounts.views.login'),
    url(r'^logout/$', 'accounts.views.logout'),
    url(r'^register/$', 'accounts.views.register_user'),
    url(r'^register_success/$', 'accounts.views.register_success'),
    url('', include('django.contrib.auth.urls', namespace='auth')),  
    url('', include('social.apps.django_app.urls', namespace='social')),
)