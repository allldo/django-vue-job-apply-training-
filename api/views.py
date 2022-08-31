from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
@api_view(['POST'])
def add_question_to_subject(request, subject):
    subject_fr = get_object_or_404(Subject, title=subject)
    question = request.data.get('question_data')
    questions = Question.objects.filter(subject=subject_fr)
    serialized = QuestionSerializer(questions, many=True).data
    if question:
        new_question = Question.objects.create(
            question=question,
            subject=subject_fr
        )
        return Response({
            'created': True, 'new_question': new_question.question
        })
    else:
        return Response({
            'questions': serialized, 'subject': subject
        })


@csrf_exempt
@api_view(['POST'])
def delete_question(request, subject, question):
    question = get_object_or_404(Question, id=question)
    question_id = question.id
    question.delete()
    return Response({
        'data': 'deleted', 'item': question_id
    })
