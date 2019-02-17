from django.db import models

# Create your models here.

class User(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=50)
	# identifier = models.IntegerField()
	username = models.CharField(max_length=20, unique=True, blank=True, null=True)
	password = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(max_length=50, blank=True, null=True)
	group = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	role_admin = models.BooleanField(default=0)
	current_state = models.BooleanField(default=0)

	def __str__(self):
		return 'username: %s email: %s group: %d role_admin: %s current_state: %s' % (self.username, self.email, self.group, self.role_admin, self.current_state)
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
	def login_authenticate_username(self, username, password):
		return (self.username == username and self.password == password)
	def login_authenticate_email(self, email, password):
		return (self.email == email and self.password == password)
