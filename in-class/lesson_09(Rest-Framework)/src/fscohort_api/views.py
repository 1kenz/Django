from django.http import JsonResponse, response
from django.shortcuts import render
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt

from fscohort_api.serializers import StudentSerializer  #? frontend olmadığında csrf token ı hariç tutmak için
# Create your views here.

@api_view(["GET", "POST"])
def student_list_create_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_Valid():
            serializer.save()
            data = {
                "message": "Student created succesfully"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)