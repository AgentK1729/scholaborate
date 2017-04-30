from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
	user = models.ForeignKey(User)
	status = models.CharField(max_length=10)