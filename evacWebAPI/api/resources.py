from tastypie.resources import ModelResource
from tastypie import fields
from api.models import User, Location
from tastypie.authorization import Authorization

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['id', 'username', 'group', 'role_admin', 'current_state']
		filtering = {
			'username' : ['exact'],
			'group'	:	['exact']
		}
		authorization = Authorization()

class LocationResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset = Location.objects.all()
		resource_name = 'location'
		authorization = Authorization()

# class MarkSafe(ModelResource):
# 	class Meta: 
# 		queryset = User.objects.all()


