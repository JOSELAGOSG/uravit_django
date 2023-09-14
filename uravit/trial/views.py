from django.shortcuts import render, get_object_or_404, redirect
from .models import Juicio, Testigo, Victima, Perito
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



#TESTIGO Views

class TestigoDetailView(DetailView):
    template_name = 'trial/testigo/testigo_detail.html'
    model = Testigo
    context_object_name = 'testigo'

class TestigoCreateView(CreateView):
    template_name = 'trial/testigo/testigo_form.html'
    model = Testigo
    fields = ['edad', 'bool_pauta_lista', 'link_pauta_necesidades']
    
    def form_valid(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = Testigo.objects.create(
            juicio = juicio,
            edad = form.cleaned_data['edad'],
            bool_pauta_lista = form.cleaned_data['bool_pauta_lista'],
            link_pauta_necesidades = form.cleaned_data['link_pauta_necesidades']
        )

        return redirect(self.object.juicio.get_absolute_url())

#VICTIMA Views

class VictimaDetailView(DetailView):
    template_name = 'trial/victima/victima_detail.html'
    model = Victima
    context_object_name = 'victima'

class VictimaCreateView(CreateView):
    template_name = 'trial/victima/victima_form.html'
    model = Victima
    fields = ['edad', 'bool_pauta_lista', 'link_pauta_necesidades']

    def form_valid(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = Victima.objects.create(
            juicio = juicio,
            edad = form.cleaned_data['edad'],
            bool_pauta_lista = form.cleaned_data['bool_pauta_lista'],
            link_pauta_necesidades = form.cleaned_data['link_pauta_necesidades']
        )

        return redirect(self.object.juicio.get_absolute_url())

#PERITO Views

class PeritoDetailView(DetailView):
    template_name = 'trial/perito/perito_detail.html'
    model = Perito
    context_object_name = 'perito'

class PeritoCreateView(CreateView):
    template_name = 'trial/perito/perito_form.html'
    model = Perito
    fields = ['institucion']

    def form_vaild(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = Perito.objects.create(
            juicio = juicio,
            institucion = form.cleaned_data['institucion']
        )
        return redirect(self.object.juicio.get_absolute_url())