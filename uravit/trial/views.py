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
    Equipo,
)
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.core.exceptions import ObjectDoesNotExist

from django.views.defaults import permission_denied

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
    success_url = reverse_lazy('trial:perfil-list')

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
    
class ApoyoDetailView(DetailView):
    template_name = 'trial/apoyo/apoyo_detail.html'
    model = Apoyo
    context_object_name = 'apoyo'

    def get(self, request, *args, **kwargs):
        apoyo = self.get_object()

        try:
            perfil = request.user.perfil
        except Exception:
            perfil = None
        
        if apoyo.equipo_a_cargo != perfil.equipo:
            return permission_denied(request, exception="Acceso Prohibido")
        
        return super().get(request, *args, **kwargs)

'''
    ApoyoListView entrega:
        -Todos los apoyos a los usuarios staff y superusuarios
        -Los apoyos relacionados al equipo del usuario si es que el usuario tiene perfil
        -Nada si es que el usuario no tiene perfil
'''
class ApoyoListView(ListView):
    template_name = 'trial/apoyo/apoyo_list.html'
    model = Apoyo
    context_object_name = 'apoyos'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Apoyo.objects.all()
        else:
            try:
                perfil = Perfil.objects.get(usuario=user)
            except ObjectDoesNotExist:
                perfil = None

            if perfil:
                equipo = perfil.equipo
                queryset = Apoyo.objects.filter(equipo_a_cargo=equipo)
            else:
                queryset = Apoyo.objects.none()  # No hay perfil, por lo tanto, no se muestra nada
        return queryset


class ApoyoVictimaDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = Apoyo
    context_object_name = 'apoyo'
    
    def get_success_url(self):
        apoyo = self.object 
        victima_pk = apoyo.victima.pk
        return reverse_lazy('victima-detail', kwargs={'pk': victima_pk})

class ApoyoTestigoDeleteView(DeleteView):
    template_name = 'trial/apoyo/apoyo_confirm_delete.html'
    model = Apoyo
    context_object_name = 'apoyo'
    
    def get_success_url(self):
        apoyo = self.object 
        testigo_pk = apoyo.testigo.pk
        return reverse_lazy('testigo-detail', kwargs={'pk': testigo_pk})

# Mi Perfil Detail
@method_decorator(login_required, name='dispatch')
class UserPerfilView(TemplateView):
    template_name = 'trial/user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        try:
            perfil = Perfil.objects.get(usuario=user)
            context['perfil'] = perfil
            apoyos = Apoyo.objects.filter(equipo_a_cargo=perfil.equipo)
            context['apoyos'] = apoyos
        except Perfil.DoesNotExist:
            perfil = None

        return context
    
# Equipo CRUD
class EquipoCreateView(CreateView):
    template_name = 'trial/equipo/equipo_form.html'
    model = Equipo
    fields = '__all__'

class EquipoDetailView(DetailView):
    template_name = 'trial/equipo/equipo_detail.html'
    model = Equipo
    context_object_name = 'equipo'

class EquipoListView(ListView):
    template_name = 'trial/equipo/equipo_list.html'
    model = Equipo
    context_object_name = 'equipos'

class EquipoUpdateView(UpdateView):
    template_name = 'trial/equipo/equipo_form.html'
    model = Equipo
    fields = '__all__'

class EquipoDeleteView(DeleteView):
    template_name = 'trial/equipo/equipo_confirm_delete.html'
    model = Equipo
    context_object_name = 'equipo'
    success_url = reverse_lazy('trial:equipo-list')
    