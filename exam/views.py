from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
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

def exam_data(request,pk):
    exam = Exam.objects.get(id=pk)
    questions = []
    for question in exam.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.answer)
        questions.append({str(question): answers})
    return JsonResponse({
        'data': questions,
        'duration': exam.duration,
    })

def save_exam(request,pk):
    print(request.POST)
    return JsonResponse({'data': 'success'})
