from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def display_course(request):
    d={'course':Course.objects.all()}
    return render(request,'display_course.html',d)

def update_course(request):
    d={'course':Course.objects.all()}
    Course.objects.filter(cname='python').update(cname='Python')
    Course.objects.filter(cname='sql').update(cname='SQL')
    Course.objects.filter(cname='web technology').update(cname='Web Tech')
    Course.objects.filter(cname='django').update(cname='Django')
    return render(request,'display_course.html',d)


def display_student(request):
    d={'student':Student.objects.all()}
    return render(request,'display_student.html',d)

def update_student(request):
    d={'student':Student.objects.all()}
    Student.objects.filter(sname='chandu').update(sname='Chandu')
    Student.objects.filter(sname='prasad').update(marks=89)
    # TO=Course.objects.get_or_create(cid=5)[0]
    # Student.objects.update_or_create(sname='Amar',defaults={'cid':TO,'marks':80,'sid':15})
    return render(request,'display_student.html',d)