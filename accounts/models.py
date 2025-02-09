from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    standard = models.IntegerField()
    city = models.CharField(max_length=100)
    passout = models.BooleanField(default=False)

    def __str__(self):
        return self.name
