from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default="blank.png",height_field=None, width_field=None, max_length=None)
    location = models.CharField(max_length=50, blank=True)

# Create your models here.

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField( max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class FollowerCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    
    def __str__(self):
        return self.user
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to='post_images', default=None,  height_field=None, width_field=None, max_length=None)
    caption = models.TextField( )
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    
    def __str__(self):
        return self.user