from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('crear_autor/', login_required(CrearAutor.as_view()), name = 'crear_autor'),
    path('listar_autor/', login_required(ListadoAutor.as_view()), name = 'listar_autor'),
    path('editar_autor/<int:pk>/', login_required(ActualizarAutor.as_view()), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>/', login_required(EliminarAutor.as_view()), name = 'eliminar_autor'),
    
    path('listar_libros/', login_required(ListadoLibro.as_view()), name = 'listado_libros'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name = 'crear_libro'),
    path('editar_libro/<int:pk>/', login_required(ActualizarLibro.as_view()), name = 'editar_libro'),
    path('eliminar_libro/<int:pk>/', login_required(EliminarLibro.as_view()), name = 'eliminar_libro'),
    
    path('listar_mesas/', login_required(ListadoMesa.as_view()), name = 'listado_mesas'),
    path('crear_mesa/', login_required(CrearMesa.as_view()), name = 'crear_mesa'),
    path('editar_mesa/<int:pk>/', login_required(ActualizarMesa.as_view()), name = 'editar_mesa'),
    path('eliminar_mesa/<int:pk>/', login_required(EliminarMesa.as_view()), name = 'eliminar_mesa'),
    
    path('listar_recetas/', login_required(ListadoReceta.as_view()), name = 'listado_recetas'),
    path('crear_receta/', login_required(CrearReceta.as_view()), name = 'crear_receta'),
    path('editar_receta/<int:pk>/', login_required(ActualizarReceta.as_view()), name = 'editar_receta'),
    path('eliminar_receta/<int:pk>/', login_required(EliminarReceta.as_view()), name = 'eliminar_receta'),
]