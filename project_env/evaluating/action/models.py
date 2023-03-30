from django.db import models


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
    date=models.DateField()
    patient_type=models.CharField(max_length=50)
    complexity_level=models.CharField( max_length=1,choices=levels)
    status_number=models.PositiveSmallIntegerField(choices=statuses)
    #The relationsip with Action Table 
    Action=models.ForeignKey(Action,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Action.name+"/"+self.place
    