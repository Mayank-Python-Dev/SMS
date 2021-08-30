from django.contrib import admin

# Register your models here.


from django.db.models import fields

# Register your models here.

from .models import *


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['School_Name']
    list_filter = ('School_Name',)

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['School_Name', 'Teacher_Name','Teacher_Address', 'Teacher_Joining_Date']
    list_filter = ('School_Name', 'Teacher_Name','Teacher_Address', 'Teacher_Joining_Date')

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['School_Name', 'Teacher_Name',
                        'Student_Name', 'Student_Roll_No', 'Student_File']
    list_filter = ('School_Name_id', 'Teacher_Name',
                        'Student_Name',  'Student_Roll_No', 'Student_File')


    # def has_delete_permission(self, request, obj=None):
    #     return False