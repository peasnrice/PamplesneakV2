# myapp/api.py
from tastypie.resources import ModelResource

from thirdauth.models import Name


class NameResource(ModelResource):
    class Meta:
        queryset = Name.objects.all()
        resource_name = 'name'
