from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'demo.html')



def second(request):
    return render(request,'product.html')


class Student:
    pass


def third(request):
    if request.method == 'POST':
        name = request.POST['name']
        mark = request.POST['mark']
        place =request.POST['place']
        student = Student(name=name, mark=mark, place=place)
        student.save()
    return render(request, 'student.html')