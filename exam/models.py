from django.db import models
import random
from accounts.models import User
# Create your models here.

class Exam(models.Model):
    tester = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    total_marks = models.IntegerField(default="10")
    number_of_questions = models.IntegerField(default="4")
    duration = models.IntegerField(help_text="Duration of the exam in minutes", default="1")

    def __str__(self):
        return self.name

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question
    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks}"