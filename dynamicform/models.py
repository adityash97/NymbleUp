
from django.db import models
from django.forms import ModelForm

# Create your models here.
question_choices = (
    (1, 'yes/no'),
    (2,'text'),
    (3,'numberic'),
)
class Question(models.Model):
    title = models.CharField(max_length=500,blank=False)
    responseType = models.SmallIntegerField(choices=question_choices,blank=False ,default=2)
    mandatory = models.BooleanField(default=True)

    def __str__(self):
        return self.title
        


answer_choices = (
    (1, 'YES'),
    (2,'NO'),
)
class Response(models.Model):
    
    questionId = models.ForeignKey(Question,on_delete=models.CASCADE)
    answerType1 = models.CharField(max_length=4,choices=answer_choices,blank=True)
    answerType2 = models.TextField(max_length=500,blank=True)
    answerType3 = models.IntegerField(blank=True)

    def __str__(self):
        return self.id


