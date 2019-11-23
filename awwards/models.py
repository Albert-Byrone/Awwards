from django.db import models
import datetime as dt


class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')