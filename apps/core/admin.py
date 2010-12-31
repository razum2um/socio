from django.contrib import admin
from models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin (admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)