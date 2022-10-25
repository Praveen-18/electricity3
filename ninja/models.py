from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    # password=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class poweroff(models.Model):
    place = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    Off_time = models.TimeField(max_length=100)
    On_time = models.TimeField(max_length=100)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.place
class form1(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    email=models.EmailField()
    complaints=models.TextField()


    def _str_(self):
        return self.name


