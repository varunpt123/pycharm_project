from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=250)
    mark = models.IntegerField()
    place = models.TextField(max_length=250)


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.FileField(upload_to='images/')
    address = models.TextField(max_length=250)

