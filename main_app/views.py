from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Coral , CoralTraits
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
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
    def get_success_url(self):
        return reverse ('coral_detail', kwargs ={'pk':self.object.pk})

class CoralDetail(DetailView):
    model= Coral
    template_name ='coral_detail.html'

class CoralUpdate(UpdateView):
     model=Coral
     fields =['name', 'img','info',]
     template_name = "coral_update.html"
     def get_success_url(self):
        return reverse ('coral_detail', kwargs ={'pk':self.object.pk})
     
class CoralDelete(DeleteView):
     model=Coral
     fields =['name', 'img','info',]
     template_name = "coral_delete.html"
     def get_success_url(self):
        return reverse('coral_list')
     
class CoralTraitsCreate(View):

    def post(self, request, pk):
        diet= request.POST.get("diet")
        toxicity = request.POST.get("toxicity")
        rareity = request.POST.get("rareity")
        coral = Coral.objects.get(pk=pk)
        CoralTraits.objects.create(diet=diet, toxicity=toxicity, rareity=rareity)
        return redirect('coral_detail', pk=pk)