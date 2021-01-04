from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.
def home_view(request):
    form = StudentForm()
    # context = {
    #     "title" : "<b>clarusway</b>",
    #     "dict_1" : {"django" : "best framework"},
    #     "my_list" : [2,3,5,6], 
    #     "form": form
    # }
    # return render(request, "fscohort/home.html", context)
    return render(request, "fscohort/home.html")

# def about(request):
#     return render(request, "about.html", context)


def student_list(request):
    
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, "fscohort/student_list.html", context)