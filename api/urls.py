from django.contrib import admin
from django.urls import path
from .views import subject_list, questions_of_subject, add_question_to_subject, delete_question

app_name = 'api'

urlpatterns = [
    path('subject_list', subject_list, name='subject_list'),
    path('<str:subject>', questions_of_subject, name='subject_detail'),
    path('add_question/<str:subject>', add_question_to_subject, name='add_question_to_subject'),
    path('delete_question/<str:subject>/<int:question>', delete_question, name='delete_question')
]
