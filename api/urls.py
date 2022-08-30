from django.contrib import admin
from django.urls import path
from .views import subject_list, questions_of_subject

app_name = 'api'

urlpatterns = [
    path('subject_list', subject_list, name='subject_list'),
    path('<str:subject>', questions_of_subject, name='subject_detail'),

]
