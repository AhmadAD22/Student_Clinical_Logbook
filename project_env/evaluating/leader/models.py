from django.db import models
from student.models import Student
from evaluation.models import Evaluation,ScientificAbstract
from action.models import ActionInformation
from django.contrib.auth.models import User


class EvaluationPeper (models.Model):
    date=models.DateField()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    actioninfo=models.ForeignKey(ActionInformation,on_delete=models.SET_NULL,null=True)
    evaluation=models.ForeignKey(Evaluation,on_delete=models.CASCADE)
    abstract=models.ForeignKey(ScientificAbstract,on_delete=models.SET_NULL,null=True)
    leader=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.student.first_name +"/"+self.leader.first_name


