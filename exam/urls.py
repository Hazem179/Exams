from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:pk>/", views.exam_detail, name="exam_detail"),
    path("<int:pk>/data/", views.exam_data, name="exam_data"),
    path("<int:pk>/save/", views.save_exam, name="save_exam"),

]
