from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


app_name = 'trial'

urlpatterns = [
    path('', login_required(views.JuicioListView.as_view()), name='juicio-list'),

    # Juicio CRUD
    path('juicio/create/', staff_member_required(views.JuicioCreateView.as_view()), name='juicio-create'),
    path('juicio/<int:pk>/', login_required(views.JuicioDetailView.as_view()), name='juicio-detail'),
    path('juicio/<int:pk>/update/', login_required(views.JuicioUpdateView.as_view()), name='juicio-update'),
    path('juicio/<int:pk>/delete/', login_required(views.JuicioDeleteView.as_view()), name='juicio-delete'),

    # Victima CRUD
    path('juicio/<int:juicio_pk>/create-victima/', login_required(views.VictimaCreateView.as_view()), name='victima-create'),
    path('victima/<int:pk>/', login_required(views.VictimaDetailView.as_view()), name='victima-detail'),
    path('victima/<int:pk>/update/', login_required(views.VictimaUpdateView.as_view()), name='victima-update'),
    path('victima/<int:pk>/delete/', login_required(views.VictimaDeleteView.as_view()), name='victima-delete'),
    
    # Testigo CRUD
    path('juicio/<int:juicio_pk>/create-testigo/', login_required(views.TestigoCreateView.as_view()), name='testigo-create'),
    path('testigo/<int:pk>/', login_required(views.TestigoDetailView.as_view()), name='testigo-detail'),
    path('testigo/<int:pk>/update/', login_required(views.TestigoUpdateView.as_view()), name='testigo-update'),
    path('testigo/<int:pk>/delete/', login_required(views.TestigoDeleteView.as_view()), name='testigo-delete'),
    
    # Perito CRUD
    path('juicio/<int:juicio_pk>/create-perito/', login_required(views.PeritoCreateView.as_view()), name='perito-create'),
    path('perito/<int:pk>/', login_required(views.PeritoDetailView.as_view()), name='perito-detail'),
    path('perito/<int:pk>/update/', login_required(views.PeritoUpdateView.as_view()), name='perito-update'),
    path('perito/<int:pk>/delete/', login_required(views.PeritoDeleteView.as_view()), name='perito-delete'),


    # Perfil CRUD
    path('perfil/create/', login_required(views.PerfilCreateView.as_view()), name='perfil-create'),
    path('perfil/', login_required(views.PerfilListView.as_view()), name='perfil-list'),
    path('perfil/<int:pk>/', login_required(views.PerfilDetailView.as_view()), name='perfil-detail'),
    path('perfil/<int:pk>/update/', login_required(views.PerfilUpdateView.as_view()), name='perfil-update'),
    path('perfil/<int:pk>/delete/', login_required(views.PerfilDeleteView.as_view()), name='perfil-delete'),

    # Apoyo Victima Create
    path('victima/<int:victima_pk>/create-apoyo/', login_required(views.ApoyoVictimaCreateView.as_view()), name='apoyo-victima-create'),

    # Apoyo Testigo Create
    path('testigo/<int:testigo_pk>/create-apoyo/', login_required(views.ApoyoTestigoCreateView.as_view()), name='apoyo-testigo-create'),

    # Apoyo
    path('apoyo/', views.ApoyoListView.as_view(), name='apoyo-list'),
    path('apoyo/<int:pk>/', views.ApoyoDetailView.as_view(), name='apoyo-detail'),
    path('apoyo/<int:pk>/v_delete/', views.ApoyoVictimaDeleteView.as_view(), name='apoyo-victima-delete'),
    path('apoyo/<int:pk>/t_delete/', views.ApoyoTestigoDeleteView.as_view(), name='apoyo-testigo-delete'),

    # Mi Perfil
    path('mi-perfil/', login_required(views.UserPerfilView.as_view()), name='user-perfil'),

    # Equipo CRUD
    path('equipo/', login_required(views.EquipoListView.as_view()), name='equipo-list'),
    path('equipo/create/', login_required(views.EquipoCreateView.as_view()), name='equipo-create'),
    path('equipo/<int:pk>/', login_required(views.EquipoDetailView.as_view()), name='equipo-detail'),
    path('equipo/<int:pk>/update/', login_required(views.EquipoUpdateView.as_view()), name='equipo-update'),
    path('equipo/<int:pk>/delete/', login_required(views.EquipoDeleteView.as_view()), name='equipo-delete'),

]