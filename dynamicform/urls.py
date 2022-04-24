from django.urls import path
from .views import home,createform,fillform

urlpatterns = [
    path('',home,name="home"),
    path('create/',createform,name="createform_question"),
    path('fill/',fillform,name="fillform_reponse"),
]
