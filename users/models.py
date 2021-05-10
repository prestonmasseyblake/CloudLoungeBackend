from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(null=True)
    name = models.CharField(max_length = 128, null=True)
    website = models.TextField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=10,null=True)
    numOfLounges = models.IntegerField(default=0,null=True)
    loungeFollowers = models.ManyToManyField("self", null=True, blank=True)
    loungeFollowing = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self):
        return self.email
    
    @property
    def lounges_count(self):
        return self.Lounge.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()
    
    @property
    def following_count(self):
        return self.following.all().count()

class Wallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

