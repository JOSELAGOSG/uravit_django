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

# URLs de la Aplicación de Juicios

A continuación se presentan las URLs utilizadas en la aplicación de juicios:

## Juicio CRUD

### Lista de Juicios
- **URL:** `/juicio/`
- **Vista:** `JuicioListView`
- **Descripción:** Muestra una lista de todos los juicios.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Crear Juicio
- **URL:** `/juicio/create/`
- **Vista:** `JuicioCreateView`
- **Descripción:** Permite crear un nuevo juicio.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Detalle de Juicio
- **URL:** `/juicio/<int:pk>/`
- **Vista:** `JuicioDetailView`
- **Descripción:** Muestra los detalles de un juicio.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Juicio
- **URL:** `/juicio/<int:pk>/update/`
- **Vista:** `JuicioUpdateView`
- **Descripción:** Permite actualizar un juicio existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Juicio
- **URL:** `/juicio/<int:pk>/delete/`
- **Vista:** `JuicioDeleteView`
- **Descripción:** Permite eliminar un juicio existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Victima CRUD

### Crear Víctima
- **URL:** `/juicio/<int:juicio_pk>/create-victima/`
- **Vista:** `VictimaCreateView`
- **Descripción:** Permite crear una nueva víctima relacionada con un juicio.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Detalle de Víctima
- **URL:** `/victima/<int:pk>/`
- **Vista:** `VictimaDetailView`
- **Descripción:** Muestra los detalles de una víctima.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Víctima
- **URL:** `/victima/<int:pk>/update/`
- **Vista:** `VictimaUpdateView`
- **Descripción:** Permite actualizar los detalles de una víctima existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Víctima
- **URL:** `/victima/<int:pk>/delete/`
- **Vista:** `VictimaDeleteView`
- **Descripción:** Permite eliminar una víctima existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Testigo CRUD

### Crear Testigo
- **URL:** `/juicio/<int:juicio_pk>/create-testigo/`
- **Vista:** `TestigoCreateView`
- **Descripción:** Permite crear un nuevo testigo relacionado con un juicio.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Detalle de Testigo
- **URL:** `/testigo/<int:pk>/`
- **Vista:** `TestigoDetailView`
- **Descripción:** Muestra los detalles de un testigo.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Testigo
- **URL:** `/testigo/<int:pk>/update/`
- **Vista:** `TestigoUpdateView`
- **Descripción:** Permite actualizar los detalles de un testigo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Testigo
- **URL:** `/testigo/<int:pk>/delete/`
- **Vista:** `TestigoDeleteView`
- **Descripción:** Permite eliminar un testigo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Perito CRUD

### Crear Perito
- **URL:** `/juicio/<int:juicio_pk>/create-perito/`
- **Vista:** `PeritoCreateView`
- **Descripción:** Permite crear un nuevo perito relacionado con un juicio.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Detalle de Perito
- **URL:** `/perito/<int:pk>/`
- **Vista:** `PeritoDetailView`
- **Descripción:** Muestra los detalles de un perito.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Perito
- **URL:** `/perito/<int:pk>/update/`
- **Vista:** `PeritoUpdateView`
- **Descripción:** Permite actualizar los detalles de un perito existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Perito
- **URL:** `/perito/<int:pk>/delete/`
- **Vista:** `PeritoDeleteView`
- **Descripción:** Permite eliminar un perito existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Perfil CRUD

### Crear Perfil
- **URL:** `/perfil/create/`
- **Vista:** `PerfilCreateView`
- **Descripción:** Permite crear un nuevo perfil.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Lista de Perfiles
- **URL:** `/perfil/`
- **Vista:** `PerfilListView`
- **Descripción:** Muestra una lista de todos los perfiles.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Perfil
- **URL:** `/perfil/<int:pk>/update/`
- **Vista:** `PerfilUpdateView`
- **Descripción:** Permite actualizar los detalles de un perfil existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Perfil
- **URL:** `/perfil/<int:pk>/delete/`
- **Vista:** `PerfilDeleteView`
- **Descripción:** Permite eliminar un perfil existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Apoyo Victima Create

### Crear Apoyo para Víctima
- **URL:** `/victima/<int:victima_pk>/create-apoyo/`
- **Vista:** `ApoyoVictimaCreateView`
- **Descripción:** Permite crear un nuevo apoyo para una víctima.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Apoyo Testigo Create

### Crear Apoyo para Testigo
- **URL:** `/testigo/<int:testigo_pk>/create-apoyo/`
- **Vista:** `ApoyoTestigoCreateView`
- **Descripción:** Permite crear un nuevo apoyo para un testigo.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

## Apoyo

### Lista de Apoyos
- **URL:** `/apoyo/`
- **Vista:** `ApoyoListView`
- **Descripción:** Muestra una lista de todos los apoyos.
- **Acceso:** Requiere inicio de sesión.

### Detalle de Apoyo
- **URL:** `/apoyo/<int:pk>/`
- **Vista:** `ApoyoDetailView`
- **Descripción:** Muestra los detalles de un apoyo.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Apoyo
- **URL:** `/apoyo/<int:pk>/update/`
- **Vista:** `ApoyoUpdateView`
- **Descripción:** Permite actualizar los detalles de un apoyo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Apoyo de Víctima
- **URL:** `/apoyo/<int:pk>/v-delete/`
- **Vista:** `ApoyoVictimaDeleteView`
- **Descripción:** Permite eliminar un apoyo de víctima existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Apoyo de Testigo
- **URL:** `/apoyo/<int:pk>/t-delete/`
- **Vista:** `ApoyoTestigoDeleteView`
- **Descripción:** Permite eliminar un apoyo de testigo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Estado de Apoyo
- **URL:** `/apoyo/<int:pk>/estado-update/`
- **Vista:** `ApoyoEstadoUpdateView`
- **Descripción:** Permite actualizar el estado de un apoyo existente.
- **Acceso:** Requiere inicio de sesión.

## Mi Perfil

### Detalle de Mi Perfil
- **URL:** `/mi-perfil/`
- **Vista:** `UserPerfilView`
- **Descripción:** Muestra los detalles de tu perfil de usuario.
- **Acceso:** Requiere inicio de sesión.

## Equipo CRUD

### Lista de Equipos
- **URL:** `/equipo/`
- **Vista:** `EquipoListView`
- **Descripción:** Muestra una lista de todos los equipos.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Crear Equipo
- **URL:** `/equipo/create/`
- **Vista:** `EquipoCreateView`
- **Descripción:** Permite crear un nuevo equipo.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Detalle de Equipo
- **URL:** `/equipo/<int:pk>/`
- **Vista:** `EquipoDetailView`
- **Descripción:** Muestra los detalles de un equipo.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Actualizar Equipo
- **URL:** `/equipo/<int:pk>/update/`
- **Vista:** `EquipoUpdateView`
- **Descripción:** Permite actualizar los detalles de un equipo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.

### Eliminar Equipo
- **URL:** `/equipo/<int:pk>/delete/`
- **Vista:** `EquipoDeleteView`
- **Descripción:** Permite eliminar un equipo existente.
- **Acceso:** Requiere inicio de sesión de personal con permisos.
