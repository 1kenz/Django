from django import forms
from .models import Student
# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField()
    
    # def __str__(self):
    #     return self.first_name + " " + self.last_name
    
class StudentForm(forms.ModelForm):
    
    first_name = forms.CharField(label="Your Name")  # override
    
    class Meta:
        model = Student
        fields = '__all__'
        # fields= ("first_name", "last_name")  
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["first_name"].label = "Name" # override