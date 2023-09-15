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

#ApoyoTestigoProteccionEspecial CRUD

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

class ApoyoTestigoProteccionEspecialDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_proteccion_especial_detail.html'
    model = ApoyoTestigoProteccionEspecial
    context_object_name = 'apoyo'

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












