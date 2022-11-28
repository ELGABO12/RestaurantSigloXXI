from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('listado_usuarios/', ListadoUsuario.as_view(), name='listar_usuarios'),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('editar_usuario/<int:pk>/', ActualizarUsuario.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', EliminarUsuario.as_view(), name='eliminar_usuario'),
    
    path('dashboard/', login_required(Dashboard.as_view()), name = 'dashboard'),
]

app_name = 'usuarios'