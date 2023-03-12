from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from exam.models import Exam, Question, Answer, Result
from django.shortcuts import get_object_or_404


# Create your views here.

@login_required(login_url='login')
def home(request):
    exams = Exam.objects.all()
    return render(request, 'home.html', {'exams': exams})


@login_required(login_url='login')
def exam_detail(request, pk):
    exam = Exam.objects.get(id=pk)
    return render(request, 'exams/detail.html', {'exam': exam})


def exam_data(request, pk):
    exam = Exam.objects.get(id=pk)
    questions = []
    for question in exam.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append({str(question): answers})
    return JsonResponse({
        'data': questions,
        'duration': exam.duration,
    })


def save_exam(request, pk):
    questions = []
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for key in data_.keys():
            question = Question.objects.get(text=key)
            questions.append(question)
        exam = Exam.objects.get(pk=pk)
        user = request.user

        score = 0
        multiplier = 100 / exam.number_of_questions
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.is_correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.is_correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(exam=exam, student=user, marks=score_)
        print(score_)

    return JsonResponse({'data': 'success'})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
