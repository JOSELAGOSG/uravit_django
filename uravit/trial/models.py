from django.db import models

# Create your models here.

class Juicio(models.Model):
    ruc = models.CharField(max_length=25)
    auto_apertura = models.CharField(max_length=200, null=True)
    fecha_juicio_oral = models.DateField(null=True)
    fiscal = models.CharField(max_length=30, null=True)


class Responsable(models.Model):
    TIPOS_CHOICES = [('es', 'Equipo Especial Juicios'), ('ur', 'Equipo URAVIT'), 
                     ('fi', 'Equipo Fiscal'), ('ug', 'Equipo UGI')]
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=2)
    nombre = models.CharField(max_length=30)
    id_juicio = models.ForeignKey(Juicio, related_name='responsables', on_delete=models.CASCADE)


class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
    direccion = models.CharField (max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50)  # Arreglar para los constraints 
    bool_esta_notificada = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Testigo(Persona):
    id_juicio = models.ForeignKey(Juicio, related_name="testigos", on_delete=models.CASCADE )

    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True)


class Victima(Persona):
    id_juicio = models.ForeignKey(Juicio, related_name="victimas", on_delete=models.CASCADE )

    edad = models.IntegerField(null=True)
    bool_pauta_lista = models.BooleanField(default=False)
    link_pauta_necesidades = models.URLField(null=True)

class Perito(Persona):
    id_juicio = models.ForeignKey(Juicio, related_name="peritos", on_delete=models.CASCADE )
    institucion = models.CharField(max_length=30)



class PautaNecesidadesTestigo(models.Model):
    id_testigo = models.ForeignKey(Testigo, related_name="pauta_necesidades", on_delete=models.CASCADE)
    traslado = models.TextField()
    alojamiento = models.TextField()


class PautaNecesidadesVictima(models.Model):
    id_victima = models.ForeignKey(Victima, related_name="pauta_necesidades", on_delete=models.CASCADE)
    traslado = models.TextField()
    alojamiento = models.TextField()