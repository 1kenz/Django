from django.http import JsonResponse
from django.shortcuts import render
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt  #? frontend olmadığında csrf token ı hariç tutmak için
# Create your views here.

#! RETURN A STATIC VALUE ON API
def fscohort_api(request):
    data = {
        "name": "ken",
        "surname": "den",
        "status": "perfect"
    }
    return JsonResponse(data)

@csrf_exempt
#! SERIALIZE POST
def student_create_api(request):
    if request.method == "POST":
        post_data = json.loads(request.body)
        
        name = post_data.get("first_name")
        lastname= post_data.get("last_name")
        number = post_data.get("number")
        
        student_data = {
            "first_name": name,
            "last_name": lastname,
            "number": number
        }
        
        student_object = Student.objects.create(**student_data)
        data = {
            "message": f"Student {student_object.first_name} created succesfully"
        }
        return JsonResponse(data, status=201)

#! SERIALIZE PYTHON- GET - Serialize: Bir veri tipinden başka bir veri tipine çevirme
def student_list_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_data = serialize("python", students)
        
        data = {
            "students" : student_data,
            "count" : student_count
        }
        return JsonResponse(data)


#! BASIT MODEL LERDE KULLANILABILIR- GET
# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()

#         student_list = []
#         for student in students:
#             student_list.append({
#                 "firstname": student.first_name,
#                 "lastname": student.last_name,
#                 "number": student.number
#             })
#         data = {
#             "students" : student_list,
#             "count": student_count
#         }
#         return JsonResponse(data)