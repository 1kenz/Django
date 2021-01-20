from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from ken.models import Student
# Create your views here.

def ken_api(request):
    data = {
        "name": "Ken",
        "surname": "Den",
        "skills": ["python", "django"]
    }
    return JsonResponse(data)


def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_count = Student.objects.count()
        
        student_list = []
        for student in students:
            student_list.append({
                
            })
        
        # data = {
        #     "students" : students,
        #     "count" : student_count 
        # }
        return JsonResponse(data)