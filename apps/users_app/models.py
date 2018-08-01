from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    # extends class and allows us to add more attributes to actual user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classes
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
    	# username is attribute of user object now
    	return self.user.username
