from django.urls import path, include
from . import views

app_name = 'trial'

urlpatterns = [
    path('', views.JuicioListView.as_view(), name='juicio-list'),
    path('juicio/<int:pk>/', views.JuicioDetailView.as_view(), name='juicio-detail'),
    path('juicio/create/', views.JuicioCreateView.as_view(), name = 'juicio-create'),
    path('juicio/<int:juicio_pk>/create-victima/', views.VictimaCreateView.as_view(), name='victima-create'),
    path('juicio/<int:juicio_pk>/create-testigo/', views.TestigoCreateView.as_view(), name='testigo-create'),
    path('juicio/<int:juicio_pk>/create-perito/', views.PeritoCreateView.as_view(), name='perito-create'),

    path('victima/<int:pk>/', views.VictimaDetailView.as_view(), name='victima-detail'),
]