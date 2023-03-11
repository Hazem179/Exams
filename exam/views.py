from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from exam.models import Exam


# Create your views here.

@login_required(login_url='login')
def home(request):
    exams = Exam.objects.all()
    return render(request, 'home.html', {'exams': exams})


@login_required(login_url='login')
def exam_detail(request,pk):
    exam = Exam.objects.get(id=pk)
    return render(request, 'exams/detail.html', {'exam': exam})

