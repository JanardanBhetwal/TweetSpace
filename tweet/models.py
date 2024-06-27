from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tweet=models.TextField(max_length=140)
    photos=models.ImageField(upload_to='photos/',blank=True,null=True) #blank=True means the field is not required, null=True means the field can be null in the database
    created_at=models.DateTimeField(auto_now_add=True)    # auto_now_add=True means the field will be set to now when the object is first created
    updated_at=models.DateTimeField(auto_now=True)        # auto_now=True means the field will be set to now every time the object is saved

    def __str__(self):
        return f'{self.user} tweeted {self.tweet}'         # This is the string representation of the object