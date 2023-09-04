from django.urls import path, include
from . import views

app_name = 'trial'

urlpatterns = [
    path('', views.JuicioListView.as_view(), name='juicio-list'),
    path('juicio/<int:pk>/', views.JuicioDetailView.as_view(), name='juicio-detail'),



    path('victima/<int:pk>/', views.VictimaDetailView.as_view(), name='victima-detail'),
]