from django.db import models

class Evaluation (models.Model):
    #order like evaluating paper to find by line number: n+5
  
    medicine_interview=models.PositiveSmallIntegerField(null=True,blank=True)
    pysical_examination=models.PositiveSmallIntegerField(null=True,blank=True)
    behavior=models.PositiveSmallIntegerField(null=True,blank=True)
    Counseling=models.PositiveSmallIntegerField(null=True,blank=True)
    clinical_judgment=models.PositiveSmallIntegerField(null=True,blank=True)
    organization_efficiency=models.PositiveSmallIntegerField(null=True,blank=True)
    explan_to_the_leader=models.PositiveSmallIntegerField(null=True,blank=True)
    getting_approval=models.PositiveSmallIntegerField(null=True,blank=True)
    protocol=models.PositiveSmallIntegerField(null=True,blank=True)
    providing_analgesia=models.PositiveSmallIntegerField(null=True,blank=True)
    tools=models.PositiveSmallIntegerField(null=True,blank=True)
    technical_steps=models.PositiveSmallIntegerField(null=True,blank=True)
    unexpected_events=models.PositiveSmallIntegerField(null=True,blank=True)
    communication_with_patent=models.PositiveSmallIntegerField(null=True,blank=True)
    story_method=models.PositiveSmallIntegerField(null=True,blank=True)
    story_content=models.PositiveSmallIntegerField(null=True,blank=True)
    mental_status_ex=models.PositiveSmallIntegerField(null=True,blank=True)
    data_synthesis=models.PositiveSmallIntegerField(null=True,blank=True)
    clinical_record=models.PositiveSmallIntegerField(null=True,blank=True)
    communication_and_team=models.PositiveSmallIntegerField(null=True,blank=True)
    leadership=models.PositiveSmallIntegerField(null=True,blank=True)
    nots=models.TextField(blank=True,null=True)


class ScientificAbstract(models.Model):
    
    final_level=models.CharField(max_length=10)
    summary_report=models.TextField(blank=True,null=True)
   
    

    
    

    