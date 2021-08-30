from django import forms

from .models import *


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['School_Name'].queryset = Student.objects.none()