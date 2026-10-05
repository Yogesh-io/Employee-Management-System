from django.db import models

# Create your models here.
class employee(models.Model):
    empid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=10)
    email = models.EmailField("Email Address", max_length=254, unique=True)
    password = models.CharField(max_length=128)


    def __str__(self):
        return f"{self.empid} - {self.name}"