from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Coral
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"

class About(TemplateView):
    template_name="about.html"

class CoralList(TemplateView):
    template_name="coral_list.html"
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data( **kwargs)
        context['corals'] = Coral.objects.all()
        return context
        
class CoralCreate(CreateView):
    model=Coral
    fields =['name', 'img','info',]
    template_name = "coral_create.html"
    success_url = "/coral/"

class CoralDetail(DetailView):
    model= Coral
    template_name ='coral_detail.html'