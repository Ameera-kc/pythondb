from pyexpat import model
from django.db import models

class student_details(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField
    mail=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


