from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('crear_producto/', login_required(CrearProducto.as_view()), name = 'crear_producto'),
    path('listar_producto/', login_required(ListadoProducto.as_view()), name = 'listar_producto'),
    path('editar_producto/<int:pk>/', login_required(ActualizarProducto.as_view()), name = 'editar_producto'),
    path('eliminar_producto/<int:pk>/', login_required(EliminarProducto.as_view()), name = 'eliminar_producto'),
    
    path('listar_proveedores/', login_required(ListadoProveedor.as_view()), name = 'listado_proveedores'),
    path('crear_proveedor/', login_required(CrearProveedor.as_view()), name = 'crear_proveedor'),
    path('editar_proveedor/<int:pk>/', login_required(ActualizarProveedor.as_view()), name = 'editar_proveedor'),
    path('eliminar_proveedor/<int:pk>/', login_required(EliminarProveedor.as_view()), name = 'eliminar_proveedor'),
    
    path('listar_mesas/', login_required(ListadoMesa.as_view()), name = 'listado_mesas'),
    path('crear_mesa/', login_required(CrearMesa.as_view()), name = 'crear_mesa'),
    path('editar_mesa/<int:pk>/', login_required(ActualizarMesa.as_view()), name = 'editar_mesa'),
    path('eliminar_mesa/<int:pk>/', login_required(EliminarMesa.as_view()), name = 'eliminar_mesa'),
    
    path('listar_recetas/', login_required(ListadoReceta.as_view()), name = 'listado_recetas'),
    path('crear_receta/', login_required(CrearReceta.as_view()), name = 'crear_receta'),
    path('editar_receta/<int:pk>/', login_required(ActualizarReceta.as_view()), name = 'editar_receta'),
    path('eliminar_receta/<int:pk>/', login_required(EliminarReceta.as_view()), name = 'eliminar_receta'),
    
    path('listar_orden/', login_required(ListadoOrden.as_view()), name = 'lista_ordenes'),
    path('detalle_orden/<int:pk>', login_required(DetalleOrden.as_view()), name ='detalle_orden'),

    path('listar_bodegas/', login_required(ListadoBodega.as_view()), name = 'listado_bodegas'),
    path('crear_bodega/', login_required(CrearBodega.as_view()), name = 'crear_bodega'),
    path('editar_bodega/<int:pk>/', login_required(ActualizarBodega.as_view()), name = 'editar_bodega'),
    path('eliminar_bodega/<int:pk>/', login_required(EliminarBodega.as_view()), name = 'eliminar_bodega'),
]

app_name = 'mantenedor'