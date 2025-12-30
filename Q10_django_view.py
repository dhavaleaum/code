
from django.shortcuts import render
from .models import Student

def mca_students(request):
    students = Student.objects.filter(course="MCA", marks__gt=75)
    return render(request, "result.html", {"students": students})
