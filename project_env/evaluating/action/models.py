from django.db import models
from student.models import Student

class Action (models.Model):
    # Table fields
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name+"/type:"+self.type

class ActionInformation(models.Model):
    # Complexity level map
    levels=(('L','Low'),('M','Medium'),('H','High'))
    statuses=((1,1),(2,2),(3,3),(4,4))
    
    # Table fields
    place=models.CharField(max_length=250)
    patient_type=models.CharField(max_length=100)
    complexity_level=models.CharField(max_length=1,choices=levels)
    case_number=models.PositiveSmallIntegerField(choices=statuses)
    #The relationsip with Action Table 
    Action=models.ForeignKey(Action,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.Action.name+"/"+self.place
    
# Aaaign the students to an actions 
class ActionToStudent(models.Model):
    action=models.ForeignKey(Action,on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    done=models.BooleanField()
    case_num=models.PositiveSmallIntegerField()
    