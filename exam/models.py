from django.db import models
from accounts.models import User
# Create your models here.

class Exam(models.Model):
    tester = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    total_marks = models.IntegerField(default="10")
    duration = models.IntegerField(help_text="Duration of the exam in minutes", default="1")

    def __str__(self):
        return self.name

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    answer_a = models.TextField()
    answer_b = models.TextField()
    answer_c = models.TextField()
    answer_d = models.TextField()
    correct_answer = models.CharField(max_length=1, help_text="Enter the correct answer in capital letter")

    def __str__(self):
        return self.question


class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks}"