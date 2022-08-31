from django.contrib import admin
from .models import Question, Subject


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'subject')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Subject)
