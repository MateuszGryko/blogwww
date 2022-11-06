from django.contrib import admin
from .models import Question, Choice

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']
    
@admin.register(Choice)

class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['votes', 'answer', 'choice_text', 'question']
    search_fields = ['choice_text', 'answer']
    