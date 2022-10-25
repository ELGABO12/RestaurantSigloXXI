from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from apps.mantenedor.forms import ProductoForm
from .models import Producto

# def login(request):
#     return render(request, 'login.html')

# def generales(request):
#     return render(request, 'generales.html')



def crearProducto(request):
    if request.method == 'POST':
        print(request.POST)
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('index')
    else:
        producto_form = ProductoForm()
    return render(request, 'mantenedor/crear_producto.html', {'producto_form':producto_form})


def listarProducto(request):
    productos = Producto.objects.filter(estado = True)
    return render(request, 'mantenedor/listar_producto.html', {'productos':productos})


def editarProducto(request, id):
    producto_form = None
    error = None
    try:
        producto = Producto.objects.get(id = id)
        if request.method == 'GET':
            producto_form = ProductoForm(instance = producto)
        else:
            producto_form = ProductoForm(request.POST, instance = producto)
            if producto_form.is_valid():
                producto_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'mantenedor/crear_producto.html', {'producto_form':producto_form, 'error':error})


def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('mantenedor:listar_producto')
    return render(request, 'mantenedor/eliminar_producto.html', {'producto':producto})