from django.urls import path, include
from . import views

app_name = 'trial'

urlpatterns = [
    path('', views.JuicioListView.as_view(), name='juicio-list'),

    # Juicio CRUD
    path('juicio/create/', views.JuicioCreateView.as_view(), name='juicio-create'),
    path('juicio/<int:pk>/', views.JuicioDetailView.as_view(), name='juicio-detail'),
    path('juicio/<int:pk>/update/', views.JuicioUpdateView.as_view(), name='juicio-update'),
    path('juicio/<int:pk>/delete/', views.JuicioDeleteView.as_view(), name='juicio-delete'),

    # Victima CRUD
    path('juicio/<int:juicio_pk>/create-victima/', views.VictimaCreateView.as_view(), name='victima-create'),
    path('victima/<int:pk>/', views.VictimaDetailView.as_view(), name='victima-detail'),
    path('victima/<int:pk>/update/', views.VictimaUpdateView.as_view(), name='victima-update'),
    path('victima/<int:pk>/delete/', views.VictimaDeleteView.as_view(), name='victima-delete'),
    # Testigo CRUD
    path('juicio/<int:juicio_pk>/create-testigo/', views.TestigoCreateView.as_view(), name='testigo-create'),
    path('testigo/<int:pk>/', views.TestigoDetailView.as_view(), name='testigo-detail'),
    path('testigo/<int:pk>/update/', views.TestigoUpdateView.as_view(), name='testigo-update'),
    path('testigo/<int:pk>/delete/', views.TestigoDeleteView.as_view(), name='testigo-delete'),
    
    # Perito CRUD
    path('juicio/<int:juicio_pk>/create-perito/', views.PeritoCreateView.as_view(), name='perito-create'),
    path('perito/<int:pk>/', views.PeritoDetailView.as_view(), name='perito-detail'),
    path('perito/<int:pk>/update/', views.PeritoUpdateView.as_view(), name='perito-update'),
    path('perito/<int:pk>/delete/', views.PeritoDeleteView.as_view(), name='perito-delete'),

    # ApoyoVictimaTraslado CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-traslado/', views.ApoyoVictimaTrasladoCreateView.as_view(), name='apoyo-victima-traslado-create'),
    path('apoyo-victima-traslado/<int:pk>/', views.ApoyoVictimaTrasladoDetailView.as_view(), name='apoyo-victima-traslado-detail'),
    path('apoyo-victima-traslado/<int:pk>/update/', views.ApoyoVictimaTrasladoUpdateView.as_view(), name='apoyo-victima-traslado-update'),
    path('apoyo-victima-traslado/<int:pk>/delete/', views.ApoyoVictimaTrasladoDeleteView.as_view(), name='apoyo-victima-traslado-delete'),

    # ApoyoTestigoTraslado CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-traslado/', views.ApoyoTestigoTrasladoCreateView.as_view(), name='apoyo-testigo-traslado-create'),
    path('apoyo-testigo-traslado/<int:pk>/', views.ApoyoTestigoTrasladoDetailView.as_view(), name='apoyo-testigo-traslado-detail'),
    path('apoyo-testigo-traslado/<int:pk>/update/', views.ApoyoTestigoTrasladoUpdateView.as_view(), name='apoyo-testigo-traslado-update'),
    path('apoyo-testigo-traslado/<int:pk>/delete/', views.ApoyoTestigoTrasladoDeleteView.as_view(), name='apoyo-testigo-traslado'),

    # ApoyoVictimaEstadia CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-estadia/', views.ApoyoVictimaEstadiaCreateView.as_view(), name='apoyo-victima-estadia-create'),
    path('apoyo-victima-estadia/<int:pk>/', views.ApoyoVictimaEstadiaDetailView.as_view(), name='apoyo-victima-estadia-detail'),
    path('apoyo-victima-estadia/<int:pk>/update/', views.ApoyoVictimaEstadiaUpdateView.as_view(), name='apoyo-victima-estadia-update'),
    path('apoyo-victima-estadia/<int:pk>/', views.ApoyoVictimaEstadiaDeleteView.as_view(), name='apoyo-victima-estadia-delete'),

    # ApoyoTestigoEstadia CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-estadia/', views.ApoyoTestigoEstadiaCreateView.as_view(), name='apoyo-testigo-estadia-create'),
    path('apoyo-testigo-estadia/<int:pk>/', views.ApoyoTestigoEstadiaDetailView.as_view(), name='apoyo-testigo-estadia-detail'),

    # ApoyoVictimaAlimentacion CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-alimentacion/', views.ApoyoVictimaAlimentacionCreateView.as_view(), name='apoyo-victima-alimentacion-create'),
    path('apoyo-victima-alimentacion/<int:pk>/', views.ApoyoVictimaAlimentacionDetailView.as_view(), name='apoyo-victima-alimentacion-detail'),
    path('apoyo-victima-alimentacion/<int:pk>/update/', views.ApoyoVictimaAlimentacionUpdateView.as_view(), name='apoyo-victima-alimentacion-update'),
    path('apoyo-victima-alimentacion/<int:pk>/delete/', views.ApoyoVictimaAlimentacionDeleteView.as_view(), name='apoyo-victima-alimentacion-delete'),

    # ApoyoTestigoAlimentacion CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-alimentacion/', views.ApoyoTestigoAlimentacionCreateView.as_view(), name='apoyo-testigo-alimentacion-create'),
    path('apoyo-testigo-alimentacion/<int:pk>/', views.ApoyoTestigoAlimentacionDetailView.as_view(), name='apoyo-testigo-alimentacion-detail'),
    path('apoyo-testigo-alimentacion/<int:pk>/update/', views.ApoyoTestigoAlimentacionUpdateView.as_view(), name='apoyo-testigo-alimentacion-update'),
    path('apoyo-testigo-alimentacion/<int:pk>/delete/', views.ApoyoTestigoAlimentacionDeleteView.as_view(), name='apoyo-testigo-alimentacion-delete'),

    # ApoyoVictimaAsistenciaMedica CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-asistencia-medica/', views.ApoyoVictimaAsistenciaMedicaCreateView.as_view(), name='apoyo-victima-asistencia-medica-create'),
    path('apoyo-victima-asistencia-medica/<int:pk>/', views.ApoyoVictimaAsistenciaMedicaDetailView.as_view(), name='apoyo-victima-asistencia-medica-detail'),
    path('apoyo-victima-asistencia-medica/<int:pk>/update/', views.ApoyoVictimaAsistenciaMedicaUpdateView.as_view(), name='apoyo-victima-asistencia-medica-update'),
    path('apoyo-victima-asistencia-medica/<int:pk>/delete/', views.ApoyoVictimaAsistenciaMedicaDeleteView.as_view(), name='apoyo-victima-asistencia-medica-delete'),

    # ApoyoTestigoAsistenciaMedica CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-asistencia-medica/', views.ApoyoTestigoAsistenciaMedicaCreateView.as_view(), name='apoyo-testigo-asistencia-medica-create'),
    path('apoyo-testigo-asistencia-medica/<int:pk>/', views.ApoyoTestigoAsistenciaMedicaDetailView.as_view(), name='apoyo-testigo-asistencia-medica-detail'),
    path('apoyo-testigo-asistencia-medica/<int:pk>/update/', views.ApoyoTestigoAsistenciaMedicaUpdateView.as_view(), name='apoyo-testigo-asistencia-medica-update'),
    path('apoyo-testigo-asistencia-medica/<int:pk>/delete/', views.ApoyoTestigoAsistenciaMedicaDeleteView.as_view(), name='apoyo-testigo-asistencia-medica-delete'),

    # ApoyoVictimaProteccionEspecial CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-proteccion-especial/', views.ApoyoVictimaProteccionEspecialCreateView.as_view(), name='apoyo-victima-proteccion-especial-create'),
    path('apoyo-victima-proteccion-especial/<int:pk>/', views.ApoyoVictimaProteccionEspecialDetailView.as_view(), name='apoyo-victima-proteccion-especial-detail'),
    path('apoyo-victima-proteccion-especial/<int:pk>/update/', views.ApoyoVictimaProteccionEspecialUpdateView.as_view(), name='apoyo-victima-proteccion-especial-update'),
    path('apoyo-victima-proteccion-especial/<int:pk>/delete/', views.ApoyoVictimaProteccionEspecialDeleteView.as_view(), name='apoyo-victima-proteccion-especial-delete'),

    # ApoyoTestigoProteccionEspecial CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-proteccion-especial/', views.ApoyoTestigoProteccionEspecialCreateView.as_view(), name='apoyo-testigo-proteccion-especial-create'),
    path('apoyo-testigo-proteccion-especial/<int:pk>/', views.ApoyoTestigoProteccionEspecialDetailView.as_view(), name='apoyo-testigo-proteccion-especial-detail'),
    path('apoyo-testigo-proteccion-especial/<int:pk>/update/', views.ApoyoTestigoProteccionEspecialUpdateView.as_view(), name='apoyo-testigo-proteccion-especial-update'),
    path('apoyo-testigo-proteccion-especial/<int:pk>/delete/', views.ApoyoTestigoProteccionEspecialDeleteView.as_view(), name='apoyo-testigo-proteccion-especial-delete'),

    # ApoyoVictimaTraductor CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-traductor/', views.ApoyoVictimaTraductorCreateView.as_view(), name='apoyo-victima-traductor-create'),
    path('apoyo-victima-traductor/<int:pk>/', views.ApoyoVictimaTraductorDetailView.as_view(), name='apoyo-victima-traductor-detail'),
    path('apoyo-victima-traductor/<int:pk>/update/', views.ApoyoVictimaTraductorUpdateView.as_view(), name='apoyo-victima-traductor-update'),
    path('apoyo-victima-traductor/<int:pk>/delete/', views.ApoyoVictimaTraductorDeleteView.as_view(), name='apoyo-victima-traductor-delete'),

    # ApoyoTestigoTraductor CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-traductor/', views.ApoyoTestigoTraductorCreateView.as_view(), name='apoyo-testigo-traductor-create'),
    path('apoyo-testigo-traductor/<int:pk>/', views.ApoyoTestigoTraductorDetailView.as_view(), name='apoyo-testigo-traductor-detail'),
    path('apoyo-testigo-traductor/<int:pk>/update/', views.ApoyoTestigoTraductorUpdateView.as_view(), name='apoyo-testigo-traductor-update'),
    path('apoyo-testigo-traductor/<int:pk>/delete/', views.ApoyoTestigoTraductorDeleteView.as_view(), name='apoyo-testigo-traductor-delete'),

    # ApoyoVictimaConsular CRUD
    path('victima/<int:victima_pk>/create-apoyo-victima-consular/', views.ApoyoVictimaConsularCreateView.as_view(), name='apoyo-victima-consular-create'),
    path('apoyo-victima-consular/<int:pk>/', views.ApoyoVictimaConsularDetailView.as_view(), name='apoyo-victima-consular-detail'),
    path('apoyo-victima-consular/<int:pk>/update/', views.ApoyoVictimaConsularUpdateView.as_view(), name='apoyo-victima-consular-update'),
    path('apoyo-victima-consular/<int:pk>/delete/', views.ApoyoVictimaConsularDeleteView.as_view(), name='apoyo-victima-consular-delete'),

    # ApoyoTestigoConsular CRUD
    path('testigo/<int:testigo_pk>/create-apoyo-testigo-consular/', views.ApoyoTestigoConsularCreateView.as_view(), name='apoyo-testigo-consular-create'),
    path('apoyo-testigo-consular/<int:pk>/', views.ApoyoTestigoConsularDetailView.as_view(), name='apoyo-testigo-consular-detail'),
    path('apoyo-testigo-consular/<int:pk>/update/', views.ApoyoTestigoConsularUpdateView.as_view(), name='apoyo-testigo-consular-update'),
    path('apoyo-testigo-consular/<int:pk>/delete/', views.ApoyoTestigoConsularDeleteView.as_view(), name='apoyo-testigo-consular-delete'),



]