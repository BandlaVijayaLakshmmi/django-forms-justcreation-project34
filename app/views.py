from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def student(request):
    fto=Student()
    d={'student':fto}
    if request.method=='POST':
        Fd=Student(request.POST)
        if Fd.is_valid():
            return HttpResponse(str(Fd.cleaned_data))
    return render(request,'student.html',d)
