from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from .models import (
    Juicio,
    Testigo,
    Victima,
    Perito,
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
    

# Apoyos Views

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

class ApoyoTestigoProteccionEespecialCreateView(CreateView):
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

class ApoyoVictimaTraductorCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traductor.html'
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

class ApoyoTestigoTraductorCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_traductor.html'
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

class ApoyoVictimaConsularCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_consular_form'
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

class ApoyoTestigoConsularCreateView(CreateView):
    template_name = 'trial/apoyo/apoyo_consular_form'
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














