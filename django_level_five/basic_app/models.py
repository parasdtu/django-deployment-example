from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)#this statement is written to inherit data according to relation OneToOneField from inbuilt User class and copy that data to UserProfileInfo class.

    #other columns (example: portfolio_site, profile_pic) defined under this class will be added to this table inherited from models.User
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)#upload_to attribute uploads the image to the folder name passed into it inside MEDIA folder.

    def __str__(self):
        return self.user.username
