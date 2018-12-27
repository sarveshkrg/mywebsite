from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=10, primary_key=True)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " - " + self.mobileno
