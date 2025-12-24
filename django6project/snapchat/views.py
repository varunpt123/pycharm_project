from django.http import HttpResponse
from django.shortcuts import render, redirect

from snapchat.forms import TeacherForm
from snapchat.models import Teacher


# Create your views here.
def first(request):
    if request.method == 'POST':
        name = request.POST['name']
    return render(request, 'demo.html')
def second(request):
    return render(request,'product.html')
def third(request):
    return render(request,'index.html')

def teacher_form(request):
    form=TeacherForm()
    if request.method == 'POST':
        form=TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fourth_data')
    return render(request,'teacher.html',{'form':form})




def form2(request):
    data = Teacher.objects.all()
    return render(request,'new.html',{'data':data})

def form3(request,id):
    data = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('fifth_data')
    else:
        form = TeacherForm(instance=data)
        return render(request,'teacher.html',{'form':form})


def form4(request,id):
    getTeacher = Teacher.objects.get(id=id)
    getTeacher.delete()
    return redirect('fifth_data')