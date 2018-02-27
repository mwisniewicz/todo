from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#ADDITIONALS
	profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username