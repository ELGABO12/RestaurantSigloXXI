from ast import Del
from audioop import reverse
from typing import List
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from apps.libro.forms import AutorForm,LibroForm,MesaForm,RecetaForm,BodegaForm
from .models import Autor, Libro, Mesa, Receta, Bodega

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

"""
    1.- dispatch(): Valida la petición y elige qué método HTTP se utilizó para la solicitud.
    2.- http_method_not_allowed(): Retorna un error cuando se utiliza un método HTTP no soportado o definido.
    3.- options()
"""


class Inicio(TemplateView):
    template_name = 'index.html'
    
    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

    
    
class ListadoAutor(View): # Listado de Productos
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/listar_autor.html'
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['autores'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
        


class ActualizarAutor(UpdateView): # Actualizar Producto
    model = Autor
    template_name = 'libro/autor/autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.filter()
        return context
    


class CrearAutor(CreateView): # Crear Producto
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')
    
    
    
class EliminarAutor(DeleteView): # Eliminar Producto
    model = Autor
    success_url = reverse_lazy('libro:listar_autor')



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoLibro(View): # Listado de Proveedores
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearLibro(CreateView): # Crear Proveedor
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')



class ActualizarLibro(UpdateView): # Actualizar Proveedor
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.filter()
        return context
    


class EliminarLibro(DeleteView): # Eliminar Proveedor
    model = Libro
    success_url = reverse_lazy('libro:listado_libros')
    


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoMesa(View): # Listado de Mesas
    model = Mesa
    form_class = MesaForm
    template_name = 'libro/mesa/listar_mesa.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['mesas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearMesa(CreateView): # Crear Mesa
    model = Mesa
    form_class = MesaForm
    template_name = 'libro/mesa/crear_mesa.html'
    success_url = reverse_lazy('libro:listado_mesas')



class ActualizarMesa(UpdateView): # Actualizar Nesa
    model = Mesa
    form_class = MesaForm
    template_name = 'libro/mesa/mesa.html'
    success_url = reverse_lazy('libro:listado_mesas')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas'] = Mesa.objects.filter()
        return context
    


class EliminarMesa(DeleteView): # Eliminar Mesa
    model = Mesa
    success_url = reverse_lazy('libro:listado_mesas')



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoReceta(View): # Listado de Recetas
    model = Receta
    form_class = RecetaForm
    template_name = 'libro/receta/listar_receta.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['recetas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearReceta(CreateView): # Crear Receta
    model = Receta
    form_class = RecetaForm
    template_name = 'libro/receta/crear_receta.html'
    success_url = reverse_lazy('libro:listado_recetas')



class ActualizarReceta(UpdateView): # Actualizar Receta
    model = Receta
    form_class = RecetaForm
    template_name = 'libro/receta/receta.html'
    success_url = reverse_lazy('libro:listado_recetas')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['recetas'] = Receta.objects.filter()
        return context
    


class EliminarReceta(DeleteView): # Eliminar Receta
    model = Receta
    success_url = reverse_lazy('libro:listado_recetas')


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

class ListadoBodega(View): # Listado de la Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'libro/bodega/listar_bodega.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['bodega'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearBodega(CreateView): # Crear el Producto en la Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'libro/bodega/crear_bodega.html'
    success_url = reverse_lazy('libro:listado_bodega')



class ActualizarBodega(UpdateView): # Actualizar Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'libro/bodega/bodega.html'
    success_url = reverse_lazy('libro:listado_bodega')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['bodega'] = Bodega.objects.filter()
        return context
    


class EliminarBodega(DeleteView): # Eliminar Producto de la Bodega
    model = Bodega
    success_url = reverse_lazy('libro:listado_bodega')
