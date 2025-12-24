from django.http import HttpResponse
from django.shortcuts import render, redirect

from threads.forms import TeacherForm
from threads.models import product, Teacher


# Create your views here.
class Student:
    pass


def first(request):
    if request.method == 'POST':
        name = request.POST['name']
        mark = request.POST['mark']
        place = request.POST['place']

        student =product(name=name, mark=mark, place=place)
        student.save()
    return render(request,'demo.html')   
        
def second(request):
    return render(request, 'new.html')
def third(request):
    return render(request,'futura.html')
def fourth(request):
    return render(request, 'index.html')
def teacher_form(request):
    form=TeacherForm()
    if request.method == 'POST':
        form=TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fourth_data')
    return render(request,'teacher.html',{'form':form})

def form2(request):
    data=Teacher.objects.all()
    return render(request,'new2.html',{'data':data})



def form3(request,id):
    data=Teacher.objects.get(id=id)
    if request.method == 'POST':
        form=TeacherForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('fifth_data')
    else:
        form=TeacherForm(instance=data)
    return render(request,'update.html',{'form':form})
