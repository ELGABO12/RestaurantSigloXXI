from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('listado_usuarios/',login_required(ListadoUsuario.as_view()), name='listar_usuarios'),
    path('registrar_usuario/',login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('editar_usuario/<int:pk>/',login_required(ActualizarUsuario.as_view()), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/',login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),
]

app_name = 'usuarios'