from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import StudentModel  
from .forms import StudentForm
#display form & save data  typed in form 
def insert_Student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_Student.html", context)  
#view employee data
def view_Student(request):
    ob=Student.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_Student.html')
    return HttpResponse(temp.render(context,request))