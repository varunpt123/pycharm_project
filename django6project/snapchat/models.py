from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=250)

class Student(models.Model):
    name = models.CharField(max_length=250)
    mark = models.IntegerField()
    place = models.TextField(max_length=250)

class Hospital(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()

class Books(models.Model):
    name = models.CharField(max_length=250)
    genere = models.CharField(max_length=250)
    price = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    field = models.CharField(max_length=250)
    mobile = models.IntegerField()
    image = models.FileField(upload_to='images/')
    address = models.CharField(max_length=250)

