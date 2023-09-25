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
    ApoyoVictimaTraslado,
    ApoyoTestigoTraslado,
    ApoyoVictimaEstadia,
    ApoyoTestigoEstadia,
    ApoyoVictimaAlimentacion,
    ApoyoTestigoAlimentacion,
    ApoyoVictimaAsistenciaMedica,
    ApoyoTestigoAsistenciaMedica,
    ApoyoVictimaProteccionEspecial,
    ApoyoTestigoProteccionEspecial,
    ApoyoVictimaTraductor,
    ApoyoTestigoTraductor,
    ApoyoVictimaConsular,
    ApoyoTestigoConsular,
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



# Apoyo Victima Traslado CRUD
class ApoyoVictimaTrasladoCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traslado_form.html'
    model = ApoyoVictimaTraslado
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'vehiculo', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaTraslado.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            tipo = form.cleaned_data('tipo'),
            vehiculo = form.cleaned_data('vehiculo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaTrasladoDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_traslado_detail.html'
    model = ApoyoVictimaTraslado
    context_object_name = 'apoyo'

class ApoyoVictimaTrasladoUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_traslado_form.html'
    model = ApoyoVictimaTraslado
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'vehiculo', 'descripcion']

class ApoyoVictimaTrasladoDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaTraslado
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('victima-detail', kwargs={'pk': victima_pk}) 


#ApoyoTestigoTraslado CRUD

class ApoyoTestigoTrasladoCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traslado_form.html'
    model = ApoyoTestigoTraslado
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'vehiculo', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoTraslado.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            tipo = form.cleaned_data('tipo'),
            vehiculo = form.cleaned_data('vehiculo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoTrasladoDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_traslado_form.html'
    model = ApoyoTestigoTraslado
    context_object_name = 'apoyo'


class ApoyoTestigoTrasladoUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_traslado_form.html'
    model = ApoyoTestigoTraslado
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'vehiculo', 'descripcion']

class ApoyoTestigoTrasladoDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoTraslado
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})

#ApoyoVictimaEstadia CRUD

class ApoyoVictimaEstadiaCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_estadia_form.html'
    model = ApoyoVictimaEstadia
    fields = ['estado', 'equipo_a_cargo', 'con_alimentacion', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaEstadia.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            con_alimentacion = form.cleaned_data('con_alimentacion'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaEstadiaDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_estadia_detail.html'
    model = ApoyoVictimaEstadia
    context_object_name = 'apoyo'

class ApoyoVictimaEstadiaUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_estadia_form.html'
    model = ApoyoVictimaEstadia
    fields = ['estado', 'equipo_a_cargo', 'con_alimentacion', 'descripcion']

class ApoyoVictimaEstadiaDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaEstadia
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})

#ApoyoTestigoEstadia CRUD

class ApoyoTestigoEstadiaCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_estadia_form.html'
    model = ApoyoTestigoEstadia
    fields = ['estado', 'equipo_a_cargo', 'con_alimentacion', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoEstadia.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            con_alimentacion = form.cleaned_data('con_alimentacion'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoEstadiaDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_estadia_form.html'
    model = ApoyoTestigoEstadia
    context_object_name = 'apoyo'

class ApoyoTestigoEstadiaUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_estadia_form.html'
    model = ApoyoTestigoEstadia
    fields = ['estado', 'equipo_a_cargo', 'con_alimentacion', 'descripcion']

class ApoyoTestigoEstadiaDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoEstadia
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})



#ApoyoVictimaAlimentacion CRUD

class ApoyoVictimaAlimentacionCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_alimentacion_form.html'
    model = ApoyoVictimaAlimentacion
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaAlimentacion.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaAlimentacionDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_alimentacion_detail.html'
    model = ApoyoVictimaAlimentacion
    context_object_name = 'apoyo'



class ApoyoVictimaAlimentacionUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_alimentacion_form.html'
    model = ApoyoVictimaAlimentacion
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoVictimaAlimentacionDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaAlimentacion
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})
    


#ApoyoTestigoAlimentacion CRUD    

class ApoyoTestigoAlimentacionCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_alimentacion_form.html'
    model = ApoyoTestigoAlimentacion
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoAlimentacion.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoAlimentacionDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_alimentacion_detail.html'
    model = ApoyoTestigoAlimentacion
    context_object_name = 'apoyo'


class ApoyoTestigoAlimentacionUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_alimentacion_form.html'
    model = ApoyoTestigoAlimentacion
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoTestigoAlimentacionDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoAlimentacion
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})


#ApoyoVictimaAsistenciaMedica CRUD

class ApoyoVictimaAsistenciaMedicaCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_form.html'
    model = ApoyoVictimaAsistenciaMedica
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaAsistenciaMedica.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            tipo = form.cleaned_data('tipo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaAsistenciaMedicaDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_detail.html'
    model = ApoyoVictimaAsistenciaMedica
    context_object_name = 'apoyo'

class ApoyoVictimaAsistenciaMedicaUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_form.html'
    model = ApoyoVictimaAsistenciaMedica
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'descripcion']

class ApoyoVictimaAsistenciaMedicaDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaAsistenciaMedica
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})

#ApoyoTestigoAsistenciaMedica CRUD    

class ApoyoTestigoAsistenciaMedicaCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_form.html'
    model = ApoyoTestigoAsistenciaMedica
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoAsistenciaMedica.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            tipo = form.cleaned_data('tipo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoAsistenciaMedicaDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_detail.html'
    model = ApoyoTestigoAsistenciaMedica
    context_object_name = 'apoyo'

class ApoyoTestigoAsistenciaMedicaUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_asistencia_medica_form.html'
    model = ApoyoTestigoAsistenciaMedica
    fields = ['estado', 'equipo_a_cargo', 'tipo', 'descripcion']

class ApoyoTestigoAsistenciaMedicaDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoAsistenciaMedica
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})

#ApoyoVictimaProteccionEspecial CRUD

class ApoyoVictimaProteccionEspecialCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_form.html'
    model = ApoyoVictimaProteccionEspecial
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaProteccionEspecial.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaProteccionEspecialDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_detail.html'
    model = ApoyoVictimaProteccionEspecial
    context_object_name = 'apoyo'

class ApoyoVictimaProteccionEspecialUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_form.html'
    model = ApoyoVictimaProteccionEspecial
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoVictimaProteccionEspecialDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaProteccionEspecial
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})

#ApoyoTestigoProteccionEspecial CRUD

class ApoyoTestigoProteccionEspecialCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_form.html'
    model = ApoyoTestigoProteccionEspecial
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoProteccionEspecial.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoProteccionEspecialDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_detail.html'
    model = ApoyoTestigoProteccionEspecial
    context_object_name = 'apoyo'


class ApoyoTestigoProteccionEspecialUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_form.html'
    model = ApoyoTestigoProteccionEspecial
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoTestigoProteccionEspecialDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoProteccionEspecial
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})


#ApoyoVictimaTraductor CRUD


class ApoyoVictimaTraductorCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traductor_form.html'
    model = ApoyoVictimaTraductor
    fields = ['estado', 'equipo_a_cargo', 'idioma', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaTraductor.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            idioma = form.cleaned_data('idioma'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())

class ApoyoVictimaTraductorDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_traductor_detail.html'
    model = ApoyoVictimaTraductor
    context_object_name = 'apoyo'



class ApoyoVictimaTraductorUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_traductor_form.html'
    model = ApoyoVictimaTraductor
    fields = ['estado', 'equipo_a_cargo', 'idioma', 'descripcion']

class ApoyoVictimaTraductorDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaTraductor
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})



#ApoyoTestigoTraductor CRUD
class ApoyoTestigoTraductorCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traductor_form.html'
    model = ApoyoTestigoTraductor
    fields = ['estado', 'equipo_a_cargo', 'idioma', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoTraductor.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            idioma = form.cleaned_data('idioma'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoTraductorDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_traductor_detail.html'
    model = ApoyoTestigoTraductor
    context_object_name = 'apoyo'


class ApoyoTestigoTraductorUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_traductor_form.html'
    model = ApoyoTestigoTraductor
    fields = ['estado', 'equipo_a_cargo', 'idioma', 'descripcion']

class ApoyoTestigoTraductorDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoTraductor
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})




#ApoyoVictimaConsular CRUD
class ApoyoVictimaConsularCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_consular_form.html'
    model = ApoyoVictimaConsular
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        victima = get_object_or_404(Victima, pk=self.kwargs['victima_pk'])
        self.object = ApoyoVictimaConsular.objects.create(
            victima = victima,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.victima.get_absolute_url())
    
class ApoyoVictimaConsularDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_consular_detail.html'
    model = ApoyoVictimaConsular
    context_object_name = 'apoyo'

class ApoyoVictimaConsularUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_consular_form.html'
    model = ApoyoVictimaConsular
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoVictimaConsularDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoVictimaConsular
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('trial:victima-detail', kwargs={'pk': victima_pk})




#ApoyoTestigoConsular CRUD
class ApoyoTestigoConsularCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_consular_form.html'
    model = ApoyoTestigoConsular
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

    def form_valid(self, form):
        testigo = get_object_or_404(Testigo, pk=self.kwargs['testigo_pk'])
        self.object = ApoyoTestigoConsular.objects.create(
            testigo = testigo,
            estado = form.cleaned_data('estado'),
            equipo_a_cargo = form.cleaned_data('equipo_a_cargo'),
            descripcion = form.cleaned_data('descripcion')
        )
        return redirect(self.object.testigo.get_absolute_url())

class ApoyoTestigoConsularDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_consular_detail.html'
    model = ApoyoTestigoConsular
    context_object_name = 'apoyo'


class ApoyoTestigoConsularUpdateView(UpdateView):
    template_name = 'trial/apoyo/apoyo_consular_form.html'
    model = ApoyoTestigoConsular
    fields = ['estado', 'equipo_a_cargo', 'descripcion']

class ApoyoTestigoConsularDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = ApoyoTestigoConsular
    context_object_name = 'apoyo'

    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('trial:testigo-detail', kwargs={'pk': testigo_pk})









