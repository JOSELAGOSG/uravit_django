from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Juicio(models.Model):
    ruc = models.CharField(max_length=25)
    auto_apertura = models.CharField(max_length=200, null=True)
    fecha_juicio_oral = models.DateTimeField()
    fiscal = models.CharField(max_length=30, null=True)


    def __str__(self):
        return(f'{self.ruc}')

    def get_absolute_url(self):
        return reverse('trials:juicio-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trials:juicio-update', args=[self.pk])

    def get_create_victima_url(self):
        return reverse('trial:victima-create', args=[self.pk])

    def get_create_testigo_url(self):
        return reverse('trial:testigo-create', args=[self.pk])
    
    def get_create_perito_url(self):
        return reverse('trial:perito-create', args=[self.pk])

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
    direccion = models.CharField (max_length=200)
    correo = models.EmailField(null=True)
    telefono = models.CharField(max_length=50, null=True)  # Arreglar para los constraints 
    bool_esta_notificada = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Testigo(Persona):
    juicio = models.ForeignKey(Juicio, related_name="testigos", on_delete=models.CASCADE )
    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'
    
    def get_absolute_url(self):
        return reverse('trials:testigo-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trials:testigo-update', args=[self.pk])
    
class Victima(Persona):
    juicio = models.ForeignKey(Juicio, related_name="victimas", on_delete=models.CASCADE )

    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.nombre}'
    
    def get_absolute_url(self):
        return reverse('trials:victima-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trials:victima-update', args=[self.pk])

class Perito(Persona):
    juicio = models.ForeignKey(Juicio, related_name="peritos", on_delete=models.CASCADE )
    institucion = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('trials:perito-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('trials:perito-update', args=[self.pk])
    

ESTADO_APOYO = [('so', 'Solicitado'), ('co', 'En Coordinación'), ('ej', 'Ejecutado')]
EQUIPOS = [('es', 'Equipo Especial Juicios'), ('ur', 'Equipo URAVIT'), 
                     ('fi', 'Equipo Fiscal'), ('ug', 'Equipo UGI')]

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    equipo = models.CharField(choices=EQUIPOS, max_length=2)

# MODELOS ABSTRACTOS
class ApoyoAbstracto(models.Model):
    estado = models.CharField(choices=ESTADO_APOYO, max_length=2)
    equipo_a_cargo = models.CharField(choices=EQUIPOS, max_length=2)

    class Meta:
        abstract = True

class ApoyoTrasladoAbstracto(models.Model):
    TIPOS_CHOICES = [('lo', 'Local'), ('or', 'Otra Región')]
    VEHICULOS_CHOICES = [('tx', 'Taxi'), ('vi', 'Vehículo Institucional'), ('bs','Bus'), ('av', 'Avión')]
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=2) #Si es traslado local o desde otra region
    vehiculo = models.CharField(choices=VEHICULOS_CHOICES, max_length=2)
    descripcion = models.TextField(null=True)
    class Meta:
        abstract = True

class ApoyoEstadiaAbstracto(models.Model):
    con_alimentacion = models.BooleanField(default=False)
    descripcion = models.TextField(null=True)
    class Meta:
        abstract = True


class ApoyoAlimentacionAbstracto(models.Model):
    descripcion = models.TextField()

    class Meta:
        abstract = True

class ApoyoAsistenciaMedicaAbstracto(models.Model):
    TIPOS_CHOICES = [('pq', 'Psiquiátrica'), ('pc', 'Psicológica'), ('ot', 'Otro')]
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=2)
    descripcion = models.TextField(null=True)
    
    class Meta:
        abstract = True

class ApoyoProteccionEspecialAbstracto(models.Model):
    descripcion = models.TextField()

    class Meta:
        abstract = True

class ApoyoTraductorAbstracto(models.Model):
    idioma = models.CharField(max_length=20)
    descripcion = models.TextField(null=True)

    class Meta:
        abstract = True


class ApoyoConsularAbstracto(models.Model):
    descripcion = models.TextField()

    class Meta:
        abstract = True

# APOYOS HEREDAN DE ABSTRACTOS ANTERIORES

class ApoyoVictimaTraslado(ApoyoAbstracto, ApoyoTrasladoAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_traslado', on_delete=models.CASCADE)
    

class ApoyoTestigoTraslado(ApoyoAbstracto, ApoyoTrasladoAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_traslado', on_delete=models.CASCADE)
    

class ApoyoVictimaEstadia(ApoyoAbstracto, ApoyoEstadiaAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_estadia', on_delete=models.CASCADE)

class ApoyoTestigoEstadia(ApoyoAbstracto, ApoyoEstadiaAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_estadia', on_delete=models.CASCADE)    


class ApoyoVictimaAlimentacion(ApoyoAbstracto, ApoyoAlimentacionAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_alimentacion', on_delete=models.CASCADE)

class ApoyoTestigoAlimentacion(ApoyoAbstracto, ApoyoAlimentacionAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_alimentacion', on_delete=models.CASCADE)

class ApoyoVictimaAsistenciaMedica(ApoyoAbstracto, ApoyoAsistenciaMedicaAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_asistencia_medica', on_delete=models.CASCADE)

class ApoyoTestigoAsistenciaMedica(ApoyoAbstracto, ApoyoAsistenciaMedicaAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_asistencia_medica', on_delete=models.CASCADE)

class ApoyoVictimaProteccionEspecial(ApoyoAbstracto, ApoyoProteccionEspecialAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_proteccion_especial', on_delete=models.CASCADE)

class ApoyoTestigoProteccionEspecial(ApoyoAbstracto, ApoyoProteccionEspecialAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_proteccion_especial', on_delete=models.CASCADE)

class ApoyoVictimaTraductor(ApoyoAbstracto, ApoyoTraductorAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_traductor', on_delete=models.CASCADE)

class ApoyoTestigoTraductor(ApoyoAbstracto, ApoyoTraductorAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_traductor', on_delete=models.CASCADE)

class ApoyoVictimaConsular(ApoyoAbstracto, ApoyoConsularAbstracto):
    victima = models.ForeignKey(Victima, related_name='apoyos_consular', on_delete=models.CASCADE)

class ApoyoTestigoConsular(ApoyoAbstracto, ApoyoConsularAbstracto):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_consular', on_delete=models.CASCADE)    





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
    equipo_a_cargo = models.CharField(choices=EQUIPOS, max_length=2)
    estado = models.CharField(choices=ESTADO_APOYO, max_length=2)
    descripcion = models.TextField(null=True, blank=True)

    # Campos relacionados a Traslado
    traslado_tipo = models.CharField(choices=TIPOS_TRASLADOS_CHOICES, max_length=2, null=True, blank=True) #Si es traslado local o desde otra region
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