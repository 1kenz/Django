from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField()


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ("first_name", "last_name")


class StudentForm(forms.ModelForm):
    first_name = forms.CharField (label="Your Name")  # override

    class Meta:
        model = Student
        fields = "__all__"

    # override
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields["first_name"].label = "My name"
