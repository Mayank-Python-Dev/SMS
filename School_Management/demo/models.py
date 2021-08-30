from django.db import models

# Create your models here.
class School(models.Model):
    School_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.School_Name


class Teacher(models.Model):
    School_Name = models.ForeignKey(School, on_delete=models.CASCADE)
    Teacher_Name = models.CharField(max_length=100)
    Teacher_Address = models.TextField()
    Teacher_Joining_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.Teacher_Name)

class Student(models.Model):
    School_Name = models.ForeignKey(School, on_delete=models.CASCADE)
    Teacher_Name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Student_Name = models.CharField(max_length=100)
    Student_Roll_No = models.IntegerField()
    Student_File = models.FileField(upload_to='pdf')
    Student_Registration_Date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "{}".format(self.Student_Name)


    @property
    def get_pdf_url(self):
    	if self.Student_File and hasattr(self.Student_File, 'url'):
    		return self.Student_File.url
    	else:
    		return "/media/pdf/NSE_1_Certificate.pdf"