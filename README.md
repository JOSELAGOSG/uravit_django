# Modelos de la Aplicación de Juicios

A continuación se describen los modelos de datos utilizados en la aplicación de juicios:

## Modelo `Juicio`
- **ruc**: Un campo de caracteres que almacena el RUC del juicio.
- **auto_apertura**: Un campo de caracteres opcional para almacenar el auto de apertura.
- **fecha_juicio_oral**: Un campo de fecha y hora que representa la fecha del juicio oral.
- **fiscal**: Un campo de caracteres opcional para almacenar el nombre del fiscal encargado.

**Métodos:**
- `__str__()`: Retorna el RUC del juicio como representación de cadena.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles del juicio.
- `get_update_url()`: Retorna la URL absoluta para actualizar el juicio.
- `get_create_victima_url()`: Retorna la URL absoluta para crear una víctima relacionada con el juicio.
- `get_create_testigo_url()`: Retorna la URL absoluta para crear un testigo relacionado con el juicio.
- `get_create_perito_url()`: Retorna la URL absoluta para crear un perito relacionado con el juicio.

## Modelo `Persona`
- **nombre**: Un campo de caracteres que almacena el nombre de la persona.
- **rut**: Un campo de caracteres que almacena el RUT de la persona.
- **direccion**: Un campo de caracteres opcional para almacenar la dirección de la persona.
- **correo**: Un campo de correo electrónico opcional.
- **telefono**: Un campo de caracteres opcional para almacenar el número de teléfono de la persona.
- **bool_esta_notificada**: Un campo booleano que indica si la persona está notificada.
- **observaciones**: Un campo de texto opcional para almacenar observaciones sobre la persona.

**Nota**: Este es un modelo abstracto utilizado como base para otros modelos.

## Modelo `Testigo` (Hereda de `Persona`)
- **juicio**: Una clave externa que relaciona al testigo con un juicio.
- **edad**: Un campo entero opcional para almacenar la edad del testigo.
- **bool_pauta_lista**: Un campo booleano que indica si el testigo está en la lista de pauta.
- **link_pauta_necesidades**: Un campo URL opcional para enlazar a la pauta de necesidades del testigo.

**Métodos:**
- `__str__()`: Retorna el nombre del testigo como representación de cadena.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles del testigo.
- `get_update_url()`: Retorna la URL absoluta para actualizar el testigo.
- `get_delete_url()`: Retorna la URL absoluta para eliminar el testigo.

## Modelo `Victima` (Hereda de `Persona`)
- **juicio**: Una clave externa que relaciona a la víctima con un juicio.
- **edad**: Un campo entero opcional para almacenar la edad de la víctima.
- **bool_pauta_lista**: Un campo booleano que indica si la víctima está en la lista de pauta.
- **link_pauta_necesidades**: Un campo URL opcional para enlazar a la pauta de necesidades de la víctima.

**Métodos:**
- `__str__()`: Retorna el nombre de la víctima como representación de cadena.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles de la víctima.
- `get_update_url()`: Retorna la URL absoluta para actualizar la víctima.
- `get_delete_url()`: Retorna la URL absoluta para eliminar la víctima.

## Modelo `Perito` (Hereda de `Persona`)
- **juicio**: Una clave externa que relaciona al perito con un juicio.
- **institucion**: Un campo de caracteres que almacena la institución del perito.

**Métodos:**
- `__str__()`: Retorna el nombre del perito como representación de cadena.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles del perito.
- `get_update_url()`: Retorna la URL absoluta para actualizar el perito.
- `get_delete_url()`: Retorna la URL absoluta para eliminar el perito.

## Modelo `Equipo`
- **nombre**: Un campo de caracteres que almacena el nombre del equipo.

**Métodos:**
- `__str__()`: Retorna el nombre del equipo como representación de cadena.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles del equipo.

## Modelo `Perfil`
- **usuario**: Una clave externa que relaciona el perfil con un usuario.
- **equipo**: Una clave externa que relaciona el perfil con un equipo.

**Métodos:**
- `get_update_url()`: Retorna la URL absoluta para actualizar el perfil.
- `get_delete_url()`: Retorna la URL absoluta para eliminar el perfil.

## Modelo `Apoyo`
- **tipo**: Un campo de elección que indica el tipo de apoyo (traslado, estadía, alimentación, etc.).
- **victima**: Una clave externa que relaciona el apoyo con una víctima (opcional).
- **testigo**: Una clave externa que relaciona el apoyo con un testigo (opcional).
- **equipo_a_cargo**: Una clave externa que relaciona el apoyo con un equipo.
- **estado**: Un campo de elección que indica el estado del apoyo (solicitado, en coordinación, ejecutado).
- **descripcion**: Un campo de texto opcional para describir el apoyo en detalle.

Campos adicionales relacionados con el tipo de apoyo:
- **traslado_tipo**: Tipo de traslado (local, otra región).
- **traslado_vehiculo**: Tipo de vehículo para el traslado.
- **estadia_con_alimentacion**: Indica si la estadía incluye alimentación.
- **asistencia_medica_tipo**: Tipo de asistencia médica (psiquiátrica, psicológica, otro).
- **traductor_idioma**: Idioma para el servicio de traductor.

**Métodos:**
- `clean()`: Verifica que un apoyo no esté relacionado tanto con una víctima como con un testigo al mismo tiempo.
- `get_absolute_url()`: Retorna la URL absoluta para ver detalles del apoyo.
