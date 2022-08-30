from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, Subject
from .serializers import QuestionSerializer, SubjectSerializer


@api_view(['GET'])
def subject_list(request):
    subjects_queryset = Subject.objects.all()
    serialized = SubjectSerializer(subjects_queryset, many=True).data
    return Response({
        'subjects': serialized
    })


@api_view(['GET'])
def questions_of_subject(request, subject):
    subject_fr = get_object_or_404(Subject, title=subject)
    questions = Question.objects.filter(subject=subject_fr)
    serialized = QuestionSerializer(questions, many=True).data
    return Response({
        'questions': serialized, 'subject': subject
    })


@api_view(['POST'])
def add_question_to_subject(request, subject):
    subject_fr = get_object_or_404(Subject, title=subject)
    questions = Question.objects.filter(subject=subject_fr)
    serialized = QuestionSerializer(questions, many=True).data
    return Response({
        'questions': serialized, 'subject': subject
    })