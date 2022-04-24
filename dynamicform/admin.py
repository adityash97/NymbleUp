from django.contrib import admin
from .models import Question,Response

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title','responseType','mandatory']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id','questionId','answerType1','answerType2','answerType3']
