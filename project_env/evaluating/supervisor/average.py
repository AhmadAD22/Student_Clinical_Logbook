import pandas as pd
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from evaluation.models import Evaluation
from leader.models import EvaluationPeper
from student.models import Student
from math import isnan
from leader.functions import accept_evaluation

# Calculate total average from the result of average of pepers.
def total_average(average):
    # Get the average values from average dic
    average_values=average.values()
    #Transform average values to DataFrame for calculate the mean
    total_average=pd.DataFrame(average_values).dropna().mean()
    if isnan(total_average):
        return 'Not seen'
    else:
        return round(total_average)
    
#Calculate average for all evaluations in passed data frame.
def calculate_average(df):
    # for each evaluation standard calculate the mean (average) after delete the null values
    medicine_interview=df.medicine_interview.dropna().mean()
    pysical_examination=df.pysical_examination.dropna().mean()
    behavior=df.behavior.dropna().mean()
    Counseling=df.Counseling.dropna().mean()
    clinical_judgment=df.clinical_judgment.dropna().mean()
    organization_efficiency=df.organization_efficiency.dropna().mean()
    explan_to_the_leader=df.explan_to_the_leader.dropna().mean()
    getting_approval=df.getting_approval.dropna().mean()
    protocol=df.protocol.dropna().mean()
    providing_analgesia=df.providing_analgesia.dropna().mean()
    tools=df.tools.dropna().mean()
    technical_steps=df.technical_steps.dropna().mean()
    unexpected_events=df.unexpected_events.dropna().mean()
    communication_with_patent=df.communication_with_patent.dropna().mean()
    story_method=df.story_method.dropna().mean()
    story_content=df.story_content.dropna().mean()
    mental_status_ex=df.mental_status_ex.dropna().mean()
    data_synthesis=df.data_synthesis.dropna().mean()
    clinical_record=df.clinical_record.dropna().mean()
    communication_and_team=df.communication_and_team.dropna().mean()
    leadership=df.leadership.dropna().mean()
    #store the average standards in average dic
    average={'medicine_interview':medicine_interview,
                        'pysical_examination':pysical_examination ,
                        'behavior':behavior,
                        'Counseling':Counseling,
                        'clinical_judgment':clinical_judgment,
                        'organization_efficiency':organization_efficiency,
                        'explan_to_the_leader':explan_to_the_leader,
                        'getting_approval':getting_approval,
                        'protocol':protocol,
                        'providing_analgesia':providing_analgesia,
                        'tools':tools,
                        'technical_steps':technical_steps,
                        'unexpected_events':unexpected_events,
                        'communication_with_patent':communication_with_patent,
                        'story_method':story_method,
                        'story_content':story_content,
                        'mental_status_ex':mental_status_ex,
                        'data_synthesis':data_synthesis,
                        'clinical_record':clinical_record,
                        'communication_and_team':communication_and_team,
                        'leadership':leadership,}
    #pas
    total_av=total_average(average)
    for standard,value in average.items():
        if isnan(value):
            average[standard]="Not seen"
        else:
            average[standard]=round(value)  
    return (average,total_av)

def calcualte_null_count(df):
    medicine_interview=df.medicine_interview.isna().sum()
    pysical_examination=df.pysical_examination.isna().sum()
    behavior=df.behavior.isna().sum()
    Counseling=df.Counseling.isna().sum()
    clinical_judgment=df.clinical_judgment.isna().sum()
    organization_efficiency=df.organization_efficiency.isna().sum()
    explan_to_the_leader=df.explan_to_the_leader.isna().sum()
    getting_approval=df.getting_approval.isna().sum()
    protocol=df.protocol.isna().sum()
    providing_analgesia=df.providing_analgesia.isna().sum()
    tools=df.tools.isna().sum()
    technical_steps=df.technical_steps.isna().sum()
    unexpected_events=df.unexpected_events.isna().sum()
    communication_with_patent=df.communication_with_patent.isna().sum()
    story_method=df.story_method.isna().sum()
    story_content=df.story_content.isna().sum()
    mental_status_ex=df.mental_status_ex.isna().sum()
    data_synthesis=df.data_synthesis.isna().sum()
    clinical_record=df.clinical_record.isna().sum()
    communication_and_team=df.communication_and_team.isna().sum()
    leadership=df.leadership.isna().sum()
    count_null={ 'medicine_interview_null':medicine_interview,
                        'pysical_examination':pysical_examination ,
                        'behavior':behavior,
                        'Counseling':Counseling,
                        'clinical_judgment':clinical_judgment,
                        'organization_efficiency':organization_efficiency,
                        'explan_to_the_leader':explan_to_the_leader,
                        'getting_approval':getting_approval,
                        'protocol':protocol,
                        'providing_analgesia':providing_analgesia,
                        'tools':tools,
                        'technical_steps':technical_steps,
                        'unexpected_events':unexpected_events,
                        'communication_with_patent':communication_with_patent,
                        'story_method':story_method,
                        'story_content':story_content,
                        'mental_status_ex':mental_status_ex,
                        'data_synthesis':data_synthesis,
                        'clinical_record':clinical_record,
                        'communication_and_team':communication_and_team,
                        'leadership':leadership
    }
    return count_null
    
def average_for_student(student):
    evaluationpepers=EvaluationPeper.objects.filter(student=student)
    evaluations_id=[]
    count_of_peper_rejected=0
    count_of_peper_Acepted=0
    for evaluationpeper in evaluationpepers:
        if accept_evaluation(evaluationpeper.evaluation.id):
             evaluations_id.append(evaluationpeper.evaluation.id)
             count_of_peper_Acepted+=1
        else:
            count_of_peper_rejected +=1
    if evaluations_id:
        evaluation=Evaluation.objects.filter(id__in=evaluations_id).values()
        print(evaluations_id)
        df = pd.DataFrame(evaluation)
        average,total_average=calculate_average(df)
        count_null=calcualte_null_count(df)
        return({'average':average,'total_average':total_average,'count_null':count_null,'count_of_peper_rejected':count_of_peper_rejected,'count_of_peper_Acepted':count_of_peper_Acepted})
    else:
        return ("This Student has not accepted Evaluations")

def average_for_all_students():
    filtered_evaluations=[]
    count_of_peper_rejected=0
    count_of_peper_Acepted=0
    all_evaluations=Evaluation.objects.all()
    for evaluation in all_evaluations:
        if accept_evaluation(evaluation.id):
            filtered_evaluations.append(evaluation.id)
            count_of_peper_Acepted+=1
        else:
            count_of_peper_rejected+=1
    evaluation=Evaluation.objects.filter(id__in=filtered_evaluations).values()
    df = pd.DataFrame(evaluation)
    average,total_average=calculate_average(df)
    count_null=calcualte_null_count(df)
    return({'average':average,'total_average':total_average,'count_null':count_null,'count_of_peper_rejected':count_of_peper_rejected,'count_of_peper_Acepted':count_of_peper_Acepted})
            
class GetAverage (GenericViewSet):
    queryset=EvaluationPeper.objects.all()
    
    def specific_student (self,request,*args, **kwargs):
        student=Student.objects.get(pk=kwargs['student_id'])
        average_for_student(student)
        average_info=average_for_student(student)
        return Response({'academic_id':student.academic_number ,'first_name':student.first_name,'last_name':student.last_name,'average':average_info})
    
    def all_students(self,request):
        a=average_for_all_students()
        return Response(a)
        

