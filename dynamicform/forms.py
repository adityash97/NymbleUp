from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import Question
from django import forms

class QuestionForm(ModelForm):   
  
    class Meta: 
        model = Question
        fields = ['title','responseType','mandatory']

QuestionFormSet = modelformset_factory(Question, fields=('title','responseType','mandatory'),extra=2,)

def myform():
    fields = {}

    CHOICES =(
        (1, 'YES'),
        (2,'NO'),
        
    )
    ansType = {
        1 : forms.ChoiceField(choices = CHOICES,required=False),
        2 : forms.CharField(max_length=500,required=False),
        3 : forms.IntegerField(required=False),
        
    }
    ansTypeMandatory = {
        1 : forms.ChoiceField(choices = CHOICES),
        2 : forms.CharField(max_length=500),
        3 : forms.IntegerField(),
        
    }


    questions = Question.objects.all()
    for data in questions:
        # print("data",data)
        if data.mandatory:
            fields[data.title ] = ansTypeMandatory[data.responseType]
        else:    
            fields[data.title] = ansType[data.responseType]
    MyForm = type( 'MyForm', (forms.Form, ), fields)
    return MyForm


