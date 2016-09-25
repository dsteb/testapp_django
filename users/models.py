from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	follows = models.ManyToManyField('self', related_name='followed_by')

	def is_following(self, user_id):
		return self.follows.filter(pk=user_id).exists()
