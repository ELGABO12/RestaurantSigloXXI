from ast import Del
from audioop import reverse
from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from apps.mantenedor.forms import ProductoForm,ProveedorForm,MesaForm,RecetaForm,BodegaForm
from apps.cliente.forms import OrderCreateForm
from .models import Producto, Proveedor, Mesa, Receta, Bodega
from apps.cliente.models import *

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

"""
    1.- dispatch(): Valida la petición y elige qué método HTTP se utilizó para la solicitud.
    2.- http_method_not_allowed(): Retorna un error cuando se utiliza un método HTTP no soportado o definido.
    3.- options()
"""
    
    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

    
    
class ListadoProducto(View): # Listado de Productos
    model = Producto
    form_class = ProductoForm
    template_name = 'mantenedor/producto/listar_producto.html'
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
        


class ActualizarProducto(UpdateView): # Actualizar Producto
    model = Producto
    template_name = 'mantenedor/producto/producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('mantenedor:listar_producto')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter()
        return context
    


class CrearProducto(CreateView): # Crear Producto
    model = Producto
    form_class = ProductoForm
    template_name = 'mantenedor/producto/crear_producto.html'
    success_url = reverse_lazy('mantenedor:listar_producto')
    
    
    
class EliminarProducto(DeleteView): # Eliminar Producto
    model = Producto
    success_url = reverse_lazy('mantenedor:listar_producto')



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoProveedor(View): # Listado de Proveedores
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenedor/proveedor/listar_proveedor.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['proveedores'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearProveedor(CreateView): # Crear Proveedor
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenedor/proveedor/crear_proveedor.html'
    success_url = reverse_lazy('mantenedor:listado_proveedores')



class ActualizarProveedor(UpdateView): # Actualizar Proveedor
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'mantenedor/proveedor/proveedor.html'
    success_url = reverse_lazy('mantenedor:listado_proveedores')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.filter()
        return context
    


class EliminarProveedor(DeleteView): # Eliminar Proveedor
    model = Proveedor
    success_url = reverse_lazy('mantenedor:listado_proveedores')
    


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoMesa(View): # Listado de Mesas
    model = Mesa
    form_class = MesaForm
    template_name = 'mantenedor/mesa/listar_mesa.html'  
    
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
    template_name = 'mantenedor/mesa/crear_mesa.html'
    success_url = reverse_lazy('mantenedor:listado_mesas')



class ActualizarMesa(UpdateView): # Actualizar Nesa
    model = Mesa
    form_class = MesaForm
    template_name = 'mantenedor/mesa/mesa.html'
    success_url = reverse_lazy('mantenedor:listado_mesas')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas'] = Mesa.objects.filter()
        return context
    


class EliminarMesa(DeleteView): # Eliminar Mesa
    model = Mesa
    success_url = reverse_lazy('mantenedor:listado_mesas')



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoReceta(View): # Listado de Recetas
    model = Receta
    form_class = RecetaForm
    template_name = 'mantenedor/receta/listar_receta.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['recetas'] = self.get_queryset()
        contexto['form'] = self.form_class()
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearReceta(CreateView): # Crear Receta
    model = Receta
    form_class = RecetaForm
    template_name = 'mantenedor/receta/crear_receta.html'
    success_url = reverse_lazy('mantenedor:listado_recetas')



class ActualizarReceta(UpdateView): # Actualizar Receta
    model = Receta
    form_class = RecetaForm
    template_name = 'mantenedor/receta/receta.html'
    success_url = reverse_lazy('mantenedor:listado_recetas')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['recetas'] = Receta.objects.filter()
        return context
    


class EliminarReceta(DeleteView): # Eliminar Receta
    model = Receta
    success_url = reverse_lazy('mantenedor:listado_recetas')



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoOrden(View): # Listado de Ordenes de compra
    model = OrdenCompra
    form_class = OrderCreateForm
    template_name = 'mantenedor/orden/listar_orden.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['ordenes'] = self.get_queryset()
        contexto['form'] = self.form_class()
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class ListadoBodega(View): # Listado de la Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'mantenedor/bodega/listar_bodega.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['bodegas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearBodega(CreateView): # Crear el Producto en la Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'mantenedor/bodega/crear_bodega.html'
    success_url = reverse_lazy('mantenedor:listado_bodegas')



class ActualizarBodega(UpdateView): # Actualizar Bodega
    model = Bodega
    form_class = BodegaForm
    template_name = 'mantenedor/bodega/bodega.html'
    success_url = reverse_lazy('mantenedor:listado_bodegas')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['bodega'] = Bodega.objects.filter()
        return context
    


class EliminarBodega(DeleteView): # Eliminar Producto de la Bodega
    model = Bodega
    success_url = reverse_lazy('mantenedor:listado_bodegas')
