from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.urls import reverse_lazy
from .models import (
    Juicio,
    Testigo,
    Victima,
    Perito,
    Perfil,
    Apoyo,
)
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic import (
    ListView,
    DetailView,
)



#Juicio Views

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
    template_name = 'trial/juicio/juicio_form.html'
    model = Juicio
    fields = '__all__'

class JuicioDeleteView(DeleteView):
    template_name = 'trial/juicio/juicio_confirm_delete.html'
    model = Juicio
    context_object_name = 'juicio'
    success_url = reverse_lazy('trial:juicio-list')


#TESTIGO Views

class TestigoDetailView(DetailView):
    template_name = 'trial/testigo/testigo_detail.html'
    model = Testigo
    context_object_name = 'testigo'

class TestigoCreateView(CreateView):
    template_name = 'trial/testigo/testigo_form.html'
    model = Testigo
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'edad', 'bool_pauta_lista', 'link_pauta_necesidades']
    
    def form_valid(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = form.save(commit=False)
        self.object.juicio = juicio
        self.object.save()
        return redirect(self.object.juicio.get_absolute_url())

class TestigoUpdateView(UpdateView):
    template_name = 'trial/testigo/testigo_form.html'
    model = Testigo
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'edad', 'bool_pauta_lista', 'link_pauta_necesidades']

class TestigoDeleteView(DeleteView):
    template_name = 'trial/testigo/testigo_confirm_delete.html'
    model = Testigo
    context_object_name = 'testigo'
    
    def get_success_url(self):
        testigo = self.object
        juicio_pk = testigo.juicio.pk
        return reverse_lazy('juicio-detail', kwargs={'pk': juicio_pk})


#VICTIMA Views

class VictimaDetailView(DetailView):
    template_name = 'trial/victima/victima_detail.html'
    model = Victima
    context_object_name = 'victima'

class VictimaCreateView(CreateView):
    template_name = 'trial/victima/victima_form.html'
    model = Victima
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'edad', 'bool_pauta_lista', 'link_pauta_necesidades']

    def form_valid(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = form.save(commit=False)
        self.object.juicio = juicio
        self.object.save()
        return redirect(self.object.juicio.get_absolute_url())

class VictimaUpdateView(UpdateView):
    template_name = 'trial/victima/victima_form.html'
    model = Victima
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'edad', 'bool_pauta_lista', 'link_pauta_necesidades']

class VictimaDeleteView(DeleteView):
    template_name = 'trial/victima/victima_confirm_delete.html'
    model = Victima
    context_object_name = 'victima'
    
    def get_success_url(self):
        victima = self.object 
        juicio_pk = victima.juicio.pk
        return reverse_lazy('juicio-detail', kwargs={'pk': juicio_pk})


#PERITO Views

class PeritoDetailView(DetailView):
    template_name = 'trial/perito/perito_detail.html'
    model = Perito
    context_object_name = 'perito'

class PeritoCreateView(CreateView):
    template_name = 'trial/perito/perito_form.html'
    model = Perito
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'institucion']

    def form_valid(self, form):
        juicio = get_object_or_404(Juicio, pk=self.kwargs['juicio_pk'])
        self.object = form.save(commit=False)
        self.object.juicio = juicio
        self.object.save()
        return redirect(self.object.juicio.get_absolute_url())
    
class PeritoUpdateView(UpdateView):
    template_name = 'trial/perito/perito_form.html'
    model = Perito
    fields = ['nombre', 'rut', 'direccion', 'correo', 'telefono', 'bool_esta_notificada', 'observaciones', 'institucion']

class PeritoDeleteView(DeleteView):
    template_name = 'trial/perito/perito_confirm_delete.html'
    model = Perito
    context_object_name = 'perito'

    def get_success_url(self):
        perito = self.object 
        juicio_pk = perito.juicio.pk
        return reverse_lazy('juicio-detail', kwargs={'pk': juicio_pk})

# Perfil CRUD

class PerfilCreateView(CreateView):
    template_name = 'trial/perfil/perfil_form.html'
    model = Perfil
    fields = '__all__'

class PerfilDetailView(DetailView):
    template_name = 'trial/perfil/perfil_detail.html'
    model = Perfil
    context_object_name = 'perfil'

class PerfilListView(ListView):
    template_name = 'trial/perfil/perfil_list.html'
    model = Perfil 
    context_object_name = 'perfiles'

class PerfilUpdateView(UpdateView):
    template_name = 'trial/perfil/perfil_form.html'
    model = Perfil
    fields = '__all__'

class PerfilDeleteView(DeleteView):
    template_name = 'trial/perfil/perfil_confirm_delete.html'
    model = Perfil
    context_object_name = 'perfil'
    success_url = reverse_lazy('trial:perfil-list')

# Apoyo CRUD
class ApoyoVictimaCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_form.html'
    model = Apoyo
    fields = [
        'tipo', 
        'equipo_a_cargo',
        'estado', 
        'descripcion', 
        'traslado_tipo',
        'traslado_vehiculo',
        'estadia_con_alimentacion',
        'asistencia_medica_tipo',
        'traductor_idioma'
        ]
    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = form.save(commit=False)
        self.object.victima = victima
        self.object.save()
        print("Apoyo guardado exitosamente")
        return redirect(self.object.victima.get_absolute_url())

class ApoyoTestigoCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_form.html'
    model = Apoyo
    fields = [
        'tipo', 
        'equipo_a_cargo',
        'estado', 
        'descripcion', 
        'traslado_tipo',
        'traslado_vehiculo',
        'estadia_con_alimentacion',
        'asistencia_medica_tipo',
        'traductor_idioma'
        ]
    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = form.save(commit=False)
        self.object.testigo = testigo
        self.object.save()
        return redirect(self.object.testigo.get_absolute_url())