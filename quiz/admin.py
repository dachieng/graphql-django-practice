from django.contrib import admin
from quiz.models import Answer, Question, Quizzes, Category

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quizzes)
