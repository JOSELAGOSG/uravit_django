from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'trial'

urlpatterns = [
    path('', login_required(views.ApoyoListView.as_view()), name='home'),
    path('user/create/', staff_member_required(views.UserCreateView.as_view()), name='user-create'),
    
    # Juicio CRUD
    path('juicio/', staff_member_required(views.JuicioListView.as_view()), name='juicio-list'),
    path('juicio/create/', staff_member_required(views.JuicioCreateView.as_view()), name='juicio-create'),
    path('juicio/<int:pk>/', staff_member_required(views.JuicioDetailView.as_view()), name='juicio-detail'),
    path('juicio/<int:pk>/update/', staff_member_required(views.JuicioUpdateView.as_view()), name='juicio-update'),
    path('juicio/<int:pk>/delete/', staff_member_required(views.JuicioDeleteView.as_view()), name='juicio-delete'),

    # Victima CRUD
    path('juicio/<int:juicio_pk>/create-victima/', staff_member_required(views.VictimaCreateView.as_view()), name='victima-create'),
    path('victima/<int:pk>/', staff_member_required(views.VictimaDetailView.as_view()), name='victima-detail'),
    path('victima/<int:pk>/update/', staff_member_required(views.VictimaUpdateView.as_view()), name='victima-update'),
    path('victima/<int:pk>/delete/', staff_member_required(views.VictimaDeleteView.as_view()), name='victima-delete'),
    
    # Testigo CRUD
    path('juicio/<int:juicio_pk>/create-testigo/', staff_member_required(views.TestigoCreateView.as_view()), name='testigo-create'),
    path('testigo/<int:pk>/', staff_member_required(views.TestigoDetailView.as_view()), name='testigo-detail'),
    path('testigo/<int:pk>/update/', staff_member_required(views.TestigoUpdateView.as_view()), name='testigo-update'),
    path('testigo/<int:pk>/delete/', staff_member_required(views.TestigoDeleteView.as_view()), name='testigo-delete'),
    
    # Perito CRUD
    path('juicio/<int:juicio_pk>/create-perito/', staff_member_required(views.PeritoCreateView.as_view()), name='perito-create'),
    path('perito/<int:pk>/', staff_member_required(views.PeritoDetailView.as_view()), name='perito-detail'),
    path('perito/<int:pk>/update/', staff_member_required(views.PeritoUpdateView.as_view()), name='perito-update'),
    path('perito/<int:pk>/delete/', staff_member_required(views.PeritoDeleteView.as_view()), name='perito-delete'),

    # Perfil CRUD
    path('perfil/create/', staff_member_required(views.PerfilCreateView.as_view()), name='perfil-create'),
    path('perfil/', staff_member_required(views.PerfilListView.as_view()), name='perfil-list'),
    path('perfil/<int:pk>/update/', staff_member_required(views.PerfilUpdateView.as_view()), name='perfil-update'),
    path('perfil/<int:pk>/delete/', staff_member_required(views.PerfilDeleteView.as_view()), name='perfil-delete'),

    # Apoyo Victima Create
    path('victima/<int:victima_pk>/create-apoyo/', staff_member_required(views.ApoyoVictimaCreateView.as_view()), name='apoyo-victima-create'),

    # Apoyo Testigo Create
    path('testigo/<int:testigo_pk>/create-apoyo/', staff_member_required(views.ApoyoTestigoCreateView.as_view()), name='apoyo-testigo-create'),

    # Apoyo
    path('apoyo/', login_required(views.ApoyoListView.as_view()), name='apoyo-list'),
    path('apoyo/<int:pk>/', login_required(views.ApoyoDetailView.as_view()), name='apoyo-detail'),
    path('apoyo/<int:pk>/update/', staff_member_required(views.ApoyoUpdateView.as_view()), name='apoyo-update'),
    path('apoyo/<int:pk>/v-delete/', staff_member_required(views.ApoyoVictimaDeleteView.as_view()), name='apoyo-victima-delete'),
    path('apoyo/<int:pk>/t-delete/', staff_member_required(views.ApoyoTestigoDeleteView.as_view()), name='apoyo-testigo-delete'),
    path('apoyo/<int:pk>/estado-update/', views.ApoyoEstadoUpdateView.as_view(), name='apoyo-estado-update'),

    # Mi Perfil
    path('mi-perfil/', login_required(views.UserPerfilView.as_view()), name='user-perfil'),

    # Equipo CRUD
    path('equipo/', staff_member_required(views.EquipoListView.as_view()), name='equipo-list'),
    path('equipo/create/', staff_member_required(views.EquipoCreateView.as_view()), name='equipo-create'),
    path('equipo/<int:pk>/', staff_member_required(views.EquipoDetailView.as_view()), name='equipo-detail'),
    path('equipo/<int:pk>/update/', staff_member_required(views.EquipoUpdateView.as_view()), name='equipo-update'),
    path('equipo/<int:pk>/delete/', staff_member_required(views.EquipoDeleteView.as_view()), name='equipo-delete'),
]
