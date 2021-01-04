from django.shortcuts import render

# Create your views here.
def home_view(request):
    
    context = {
        "title" : "<b>clarusway</b>",
        "dict_1" : {"django" : "best framework"},
        "my_list" : [2,3,5,6] 
    }
    return render(request, "fscohort/home.html", context)

# def about(request):
#     return render(request, "about.html", context)