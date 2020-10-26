from django.db import models


class UserModel(models.Model):
    uemail = models.EmailField()
    uname = models.CharField(max_length=100)
    upass = models.CharField(max_length=15)
    admin = models.CharField(max_length=7)


# Create your models here.
