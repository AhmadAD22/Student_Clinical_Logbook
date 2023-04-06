from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    years=((4,4),(5,5))
    academic_number=models.PositiveIntegerField(unique=True)
    first_name=models.CharField(max_length=100)
    mid_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    academic_year=models.PositiveSmallIntegerField(choices=years)
    leader=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.first_name+' '+ self.mid_name+" "+ self.last_name

