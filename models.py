from django.db import models

# Create your models here.

class registration(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=50,null=True,blank=True)




    def __str__(self):
        return self.first_name

