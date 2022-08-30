from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')

    def __str__(self):
        return self.question
