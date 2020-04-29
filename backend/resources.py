from tastypie.resources import ModelResource
from backend.models import Scholarship
from tastypie.authorization import Authorization

class ScholarshipResource(ModelResource):
    class Meta:
        queryset = Scholarship.objects.all()
        resource_name = 'scholarship'
        authorization = Authorization()
