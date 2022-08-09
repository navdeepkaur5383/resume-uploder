from django.shortcuts import render
from .forms import Resumeform
from .models import Resume
from django.contrib import messages

from django import views
def homeviews(request):
    if request.method=='POST':
        form=Resumeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=Resumeform()

    else:
        form=Resumeform()
    details=Resume.objects.all()
    return render(request,'enroll/home.html',{'form':form,'details':details})

def details(request,id):
    de=Resume.objects.get(id=id)
    dee=Resumeform(instance=de)
    return render(request,'enroll/details.html',{"details":dee})