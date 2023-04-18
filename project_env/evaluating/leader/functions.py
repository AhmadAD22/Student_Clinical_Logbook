from evaluation.models import Evaluation
from student.models import Student
from action.models import Action,ActionToStudent
MAX_NUMBER_OF_NULL=10

def accept_evaluation(evaluatin_id):
    count=0
    evaluatin_obj=Evaluation.objects.filter(pk=evaluatin_id).values().first()
    for value in evaluatin_obj.values():
         if value == None:
            count+=1
    if count >= MAX_NUMBER_OF_NULL:
        return False
    else:
        return True
    
def handle_student_to_action(student_id,action_id,evaluatin_id):
        student_obj=Student.objects.filter(pk=student_id).first()
        action_obj=Action.objects.filter(pk=action_id).first()
        action_to_student=ActionToStudent.objects.filter(action=action_obj,student=student_obj).first()
        if action_to_student is None:
            if accept_evaluation(evaluatin_id):
                new_action_to_student=ActionToStudent.objects.create(action=action_obj,student=student_obj,done=True,case_num=1)
                new_action_to_student.save()
            else:
                new_action_to_student=ActionToStudent.objects.create(action=action_obj,student=student_obj,done=False,case_num=1)
                new_action_to_student.save()
        else:
             if accept_evaluation(evaluatin_id):
                action_to_student.done=True
                action_to_student.save()
             else:
                action_to_student.case_num+=1
                action_to_student.save()
                
                
def get_case_num(student_id,action_id):
    student_obj=Student.objects.filter(pk=student_id).first()
    action_obj=Action.objects.filter(pk=action_id).first()
    action_to_student=ActionToStudent.objects.filter(action=action_obj,student=student_obj).first()
    if action_to_student is None:
        return 1
    else:
        return action_to_student.case_num+1
            