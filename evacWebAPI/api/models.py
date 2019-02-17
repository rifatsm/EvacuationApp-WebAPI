from django.db import models

# Create your models here.

class User(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=50)
	identifier = models.IntegerField()
	current_state = models.BooleanField(default=0)
	group = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	role_admin = models.BooleanField(default=0)

	def __str__(self):
		return '%d %d %s' % (self.identifier, self.group, self.role_admin)
	def current_panic_state(self):
		return bool(self.current_state)
	def get_identifier(self):
		return self.identifier
	def get_group(self):
		return self.group
	def change_state(self):
		self.current_state = not self.current_state
		return self.current_state
	def get_role(self):
		return self.role_admin
