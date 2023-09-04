from django.shortcuts import render
from .models import Juicio, Testigo, Victima, Perito, PautaNecesidadesTestigo, PautaNecesidadesVictima
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
# Create your views here.


#Juicio CRUD

class JuicioCreateView(CreateView):
    template_name = 'trial/juicio/juicio_form.html'
    model = Juicio
    fields = '__all__'
    

class JuicioDetailView(DetailView):
    template_name = 'trial/juicio/juicio_detail.html'
    model = Juicio
    context_object_name = 'juicio'

class JuicioListView(ListView):
    template_name = 'trial/juicio/juicio_list.html'
    model = Juicio
    context_object_name = 'juicios'
     

class JuicioUpdateView(UpdateView):
    pass



class VictimaDetailView(DetailView):
    template_name = 'trial/victima/victima_detail.html'
    model = Victima
    context_object_name = 'victima'
