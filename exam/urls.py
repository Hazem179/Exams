from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path("<int:pk>/", views.exam_detail, name="exam_detail")
]