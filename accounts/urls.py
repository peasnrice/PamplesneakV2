from django.conf.urls import patterns, include, url
from api import UserResource

user_resource = UserResource()

urlpatterns = patterns('',
	url(r'^api/', include(user_resource.urls)),
)