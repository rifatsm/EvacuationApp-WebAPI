from tastypie.resources import ModelResource
from api.models import User, Location
from tastypie.authorization import Authorization

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'

class LocationResource(ModelResource):
	class Meta:
		queryset = Location.objects.all()
		resource_name = 'location'

