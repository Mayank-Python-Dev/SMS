from django.shortcuts import render , redirect

# Create your views here.
from django.contrib import messages


from .forms import *

def home(request):
	form = StudentRegistration()
	getAllData = Student.objects.all()
	if request.method == "POST":
		form = StudentRegistration(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f'SUCCESSFULLY CREATED!')
			return redirect('home')
		else:
			messages.alert(request, f'ALL FIELDS ARE REQUIRED!')
			return redirect('home')

	context = {'form':form,'getAllData':getAllData}
	return render(request,'demo/home.html',context)



def editStudent(request, pk):
	form = StudentRegistration()
	getStudent = Student.objects.get(id=pk)
	form = StudentRegistration(instance=getStudent)
	if request.method == "POST":
		form = StudentRegistration(request.POST, request.FILES, instance=getStudent)
		if form.is_valid():
			form.save()
			messages.success(request, f'SUCCESSFULLY UPDATED!')
			return redirect('home')
	context = {'form':form}
	return render(request,'demo/update.html',context)


def deleteStudent(request,pk):
	getStudent = Student.objects.get(id=pk)
	getStudent.delete()
	messages.success(request, f'DELETED!')
	return redirect('home')


def load_teacher(request):
    getSchool = request.GET.get('School_Name')
    print(getSchool)
    getTeacher = Teacher.objects.filter(School_Name=getSchool)
    print(getTeacher)
    return render(request, 'ajax/teacher_dropdown.html', {'getTeacher': getTeacher})