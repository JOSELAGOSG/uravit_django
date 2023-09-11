from django.db import models
from django.urls import reverse

# Create your models here.

class Juicio(models.Model):
    ruc = models.CharField(max_length=25)
    auto_apertura = models.CharField(max_length=200, null=True)
    fecha_juicio_oral = models.DateTimeField()
    fiscal = models.CharField(max_length=30, null=True)


    def __str__(self):
        return(f'Juicio: {self.ruc}')

    def get_absolute_url(self):
        return reverse('trials:juicio-detail', args=[self.pk])

    
'''
class Responsable(models.Model):
    TIPOS_CHOICES = [('es', 'Equipo Especial Juicios'), ('ur', 'Equipo URAVIT'), 
                     ('fi', 'Equipo Fiscal'), ('ug', 'Equipo UGI')]
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=2)
    nombre = models.CharField(max_length=30)
    id_juicio = models.ForeignKey(Juicio, related_name='responsables', on_delete=models.CASCADE)

    def __str__(self):
        return f'Responsable: {self.nombre} | {self.id_juicio}'
'''



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
    id_juicio = models.ForeignKey(Juicio, related_name="testigos", on_delete=models.CASCADE )

    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Testigo: {self.nombre} | {self.id_juicio}'

class Victima(Persona):
    id_juicio = models.ForeignKey(Juicio, related_name="victimas", on_delete=models.CASCADE )

    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True)
    
    def __str__(self):
        return f'Víctima: {self.nombre} | {self.id_juicio}'
    
    def get_absolute_url(self):
        return reverse('trials:victima-detail', args=[self.pk])

class Perito(Persona):
    id_juicio = models.ForeignKey(Juicio, related_name="peritos", on_delete=models.CASCADE )
    institucion = models.CharField(max_length=30)

    def __str__(self):
        return f'Perito: {self.nombre} | {self.id_juicio}'

class PautaNecesidadesTestigo(models.Model):
    id_testigo = models.ForeignKey(Testigo, related_name="pauta_necesidades", on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    traslado = models.TextField()
    alojamiento = models.TextField()

    def __str__(self):
        return f'Pauta Necesidades de: {self.id_testigo}'
class PautaNecesidadesVictima(models.Model):
    id_victima = models.ForeignKey(Victima, related_name="pauta_necesidades", on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    traslado = models.TextField()
    alojamiento = models.TextField()

    def __str__(self):
        return f'Pauta Necesidades de: {self.id_victima}'
    

# APOYOS
ESTADO_APOYO = [('so', 'Solicitado'), ('co', 'En Coordinación'), ('ej', 'Ejecutado')]
EQUIPOS = [('es', 'Equipo Especial Juicios'), ('ur', 'Equipo URAVIT'), 
                     ('fi', 'Equipo Fiscal'), ('ug', 'Equipo UGI')]

class ApoyoVictimaAbstracto(models.Model):
    victima = models.ForeignKey(Victima, related_name='apoyos', on_delete=models.CASCADE)
    estado = models.CharField(choices=ESTADO_APOYO, max_length=2)
    equipo_a_cargo = models.CharField(choices=EQUIPOS, max_length=2)

    class Meta:
        abstract = True

class ApoyoTestigoAbstracto(models.Model):
    testigo = models.ForeignKey(Testigo, related_name='apoyos', on_delete=models.CASCADE)
    estado = models.CharField(choices=ESTADO_APOYO, max_length=2)
    equipo_a_cargo = models.CharField(choices=EQUIPOS, max_length=2)

    class Meta:
        abstract = True

class ApoyoTrasladoAbstracto(models.Model):
    TIPOS_CHOICES = [('lo', 'Local'), ('or', 'Otra Región')]
    VEHICULOS_CHOICES = [('tx', 'Taxi'), ('vi', 'Vehículo Institucional'), ('bs','Bus'), ('av', 'Avión')]
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=2) #Si es traslado local o desde otra region
    vehiculo = models.CharField(choices=VEHICULOS_CHOICES, max_length=2)
    
    class Meta:
        abstract = True

class ApoyoVictimaTraslado(ApoyoVictimaAbstracto, ApoyoTrasladoAbstracto):
    pass

'''
class ApoyoVictimaEstadia(models.Model):
    pass

class ApoyoVictimaAlimentacion(models.Model):
    pass
class ApoyoVictimaAsistenciaMedica(models.Model):
    pass
class ApoyoVictimaProteccionEspecial(models.Model):
    pass
class ApoyoVictimaTraductor(models.Model):
    pass
class ApoyoVictimaConsular(models.Model):
    pass

class ApoyoTestigoTraslado(models.Model):
    testigo = models.ForeignKey(Testigo, related_name='apoyos_traslado', on_delete=models.CASCADE)

class ApoyoTestigoEstadia(models.Model):
    pass

class ApoyoTestigoAlimentacion(models.Model):
    pass
class ApoyoTestigoAsistenciaMedica(models.Model):
    pass
class ApoyoTestigoProteccionEspecial(models.Model):
    pass
class ApoyoTestigoTraductor(models.Model):
    pass
class ApoyoTestigoConsular(models.Model):
    pass
'''