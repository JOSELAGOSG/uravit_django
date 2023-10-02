from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Juicio(models.Model):
    ruc = models.CharField(max_length=25)
    auto_apertura = models.CharField(max_length=200, null=True, blank=True)
    fecha_juicio_oral = models.DateTimeField()
    fiscal = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.ruc}'

    def get_absolute_url(self):
        return reverse('trial:juicio-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trial:juicio-update', args=[self.pk])

    def get_create_victima_url(self):
        return reverse('trial:victima-create', args=[self.pk])

    def get_create_testigo_url(self):
        return reverse('trial:testigo-create', args=[self.pk])

    def get_create_perito_url(self):
        return reverse('trial:perito-create', args=[self.pk])

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200, blank=True)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    bool_esta_notificada = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

class Testigo(Persona):
    juicio = models.ForeignKey(Juicio, related_name="testigos", on_delete=models.CASCADE)
    edad = models.IntegerField(null=True, blank=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('trial:testigo-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trial:testigo-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('trial:testigo-delete', args=[self.pk])

class Victima(Persona):
    juicio = models.ForeignKey(Juicio, related_name="victimas", on_delete=models.CASCADE)

    edad = models.IntegerField(null=True, blank=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('trial:victima-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trial:victima-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('trial:victima-delete', args=[self.pk])

class Perito(Persona):
    juicio = models.ForeignKey(Juicio, related_name="peritos", on_delete=models.CASCADE)
    institucion = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('trial:perito-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trial:perito-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('trial:perito-delete', args=[self.pk])

ESTADO_APOYO = [('so', 'Solicitado'), ('co', 'En Coordinación'), ('ej', 'Ejecutado')]

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('trial:equipo-detail', args=[self.pk])

    def __str__(self):
        return self.nombre

    def get_update_url(self):
        return reverse('trial:equipo-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('trial:equipo-delete', args=[self.pk])

class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, related_name='perfiles', on_delete=models.CASCADE)

    def get_update_url(self):
        return reverse('trial:perfil-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('trial:perfil-delete', args=[self.pk])

class Apoyo(models.Model):
    # Choices necesarios para algunos campos
    TIPOS_APOYO_CHOICES = [('tl', 'Traslado'), ('et', 'Estadía'), ('al', 'Alimentación'), ('am', 'Asistencia Médica'), ('pe', 'Protección Especial'), ('td', 'Traductor'), ('cs', 'Consular')]
    TIPOS_TRASLADOS_CHOICES = [('lo', 'Local'), ('or', 'Otra Región')]
    VEHICULOS_CHOICES = [('tx', 'Taxi'), ('vi', 'Vehículo Institucional'), ('bs','Bus'), ('av', 'Avión')]
    TIPOS_ASISTENCIA_MEDICA_CHOICES = [('pq', 'Psiquiátrica'), ('pc', 'Psicológica'), ('ot', 'Otro')]

    tipo = models.CharField(choices=TIPOS_APOYO_CHOICES, max_length=2)

    # Campos relacionados a todos los tipos de apoyo
    victima = models.ForeignKey(Victima, related_name='apoyos', on_delete=models.CASCADE, null=True, blank=True)
    testigo = models.ForeignKey(Testigo, related_name='apoyos', on_delete=models.CASCADE, null=True, blank=True)
    equipo_a_cargo = models.ForeignKey(Equipo, related_name='apoyos', on_delete=models.CASCADE)
    estado = models.CharField(choices=ESTADO_APOYO, max_length=2)
    descripcion = models.TextField(null=True, blank=True)

    # Campos relacionados a Traslado
    traslado_tipo = models.CharField(choices=TIPOS_TRASLADOS_CHOICES, max_length=2, null=True, blank=True)  # Si es traslado local o desde otra región
    traslado_vehiculo = models.CharField(choices=VEHICULOS_CHOICES, max_length=2, null=True, blank=True)

    # Campos relacionados a Estadía
    estadia_con_alimentacion = models.BooleanField(default=False, null=True, blank=True)

    # Campos relacionados a Asistencia Médica
    asistencia_medica_tipo = models.CharField(choices=TIPOS_ASISTENCIA_MEDICA_CHOICES, max_length=2, null=True, blank=True)

    # Campos relacionados a Traductor
    traductor_idioma = models.CharField(max_length=20, null=True, blank=True)

    def clean(self):
        if self.victima and self.testigo:
            raise ValidationError("Un apoyo no puede estar relacionado tanto con una víctima como con un testigo al mismo tiempo.")

    def get_absolute_url(self):
        return reverse('trial:apoyo-detail', args=[self.pk])
