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


    # Perfil CRUD
    path('perfil/create/', views.PerfilCreateView.as_view(), name='perfil-create'),
    path('perfil/', views.PerfilListView.as_view(), name='perfil-list'),
    path('perfil/<int:pk>/', views.PerfilDetailView.as_view(), name='perfil-detail'),
    path('perfil/<int:pk>/update/', views.PerfilUpdateView.as_view(), name='perfil-update'),
    path('perfil/<int:pk>/delete/', views.PerfilDeleteView.as_view(), name='perfil-delete'),

    # Apoyo Victima CRUD
    path('victima/<int:victima_pk>/create-apoyo/', views.ApoyoVictimaCreateView.as_view(), name='apoyo-victima-create'),

    # Apoyo Testigo CRUD
    path('testigo/<int:testigo_pk>/create-apoyo/', views.ApoyoTestigoCreateView.as_view(), name='apoyo-testigo-create'),

]