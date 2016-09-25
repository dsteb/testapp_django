from django.db import models

from users.models import UserProfile

class Tweet(models.Model):
	profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	message = models.CharField(max_length=140)
	pub_datetime = models.DateTimeField('datetime published')

	def __str__(self):
		return '%s:%s' % (self.profile.user.username, self.message[20:])
