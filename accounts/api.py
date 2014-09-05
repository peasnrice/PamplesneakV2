# accounts/api.py
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
