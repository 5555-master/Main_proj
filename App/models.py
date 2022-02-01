import email
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=250)
    email=models.CharField( max_length=250)
    feedback=models.CharField(max_length=250)
    date=models.DateField()
    def __str__(self) :
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=250)
    is_verified=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.user.username


class Pick(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    forgot_token=models.CharField(max_length=250)
    

    def __str__(self):
        return self.user.username

