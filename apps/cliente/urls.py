from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('inicio_cliente/', InicioCliente.as_view(), name = 'inicio_cliente'),
    path('codigo_reserva/', CodigoReserva.as_view(), name = 'codigo_reserva'),
    
    path('listar_reservas/', login_required(ListadoReserva.as_view()), name = 'listado_reservas'),
    path('crear_reserva/', login_required(CrearReserva.as_view()), name = 'crear_reserva'),
]

app_name = 'cliente'