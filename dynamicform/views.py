from email.policy import default
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Question
from .forms import QuestionForm,QuestionFormSet,myform
from django.forms.models import modelformset_factory
from django.views.generic.edit import FormView
from django import forms






# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

home = Home.as_view()

class CreateForm(FormView):
    template_name = 'createForm.html'
    form_class = QuestionForm
    
    def get_context_data(self, **kwargs):
        context = super(CreateForm, self).get_context_data(**kwargs)
        context['formset'] = QuestionFormSet(queryset=Question.objects.none())
        return context

    def get(self,request,):
        questionForm = QuestionForm()
        # Formset = modelformset_factory(Model,form=ModelForm,extra=0)
        questionFormSet = QuestionFormSet()
        return render(request,'createForm.html',{'questionFormSet':questionFormSet})
    
    def post(self,request, *args, **kwargs):
        questionFormSet = QuestionFormSet(request.POST)
        
        # import pdb
        # pdb.set_trace()
        if questionFormSet.is_valid():
            questionFormSet.save()
            return HttpResponse("Saved")
        return HttpResponse("Not Saved")
        
createform = CreateForm.as_view()

class FillForm(TemplateView):
    template_name = 'fillForm.html'
    def get(self,request):
        return render(request, 'fillForm.html')
    def post(self,request):
        pass

def fillform(request):
    if request.method == "POST":
        
        # Save data to DB
        form = myform()
        return render(request,'fillForm.html',{'questionForm':form})


    else:
        
        form = myform()
        return render(request,'fillForm.html',{'questionForm':form})




