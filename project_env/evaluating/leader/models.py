from django.db import models
from student.models import Student
from evaluation.models import Evaluation,ScientificAbstract
from action.models import ActionInformation
from django.contrib.auth.models import User


class EvaluationPeper (models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    actioninfo=models.ForeignKey(ActionInformation,on_delete=models.CASCADE)
    evaluation=models.ForeignKey(Evaluation,on_delete=models.CASCADE)
    abstract=models.ForeignKey(ScientificAbstract,on_delete=models.CASCADE)
    leader=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.student +"/"+self.leader.first_name


