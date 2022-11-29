from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from apps.mantenedor.models import Receta, Mesa
from apps.cliente.models import Reserva, OrdenItem, OrdenCompra
from apps.cliente.forms import ReservaForm, OrderCreateForm
from apps.carrito.cart import Cart

# Create your views here.


def pedir(request):
    recetas = Receta.objects.all()
    return render(request, "cliente/area_cliente/pedir.html", {
        "recetas": recetas
    })
    

# def eleccion_mesa(request):
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             datos = form.save(commit=False)
#             datos.save()
#             for mesa in mesas:
                
                


def crear_orden(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
            for item in cart:
                OrdenItem.objects.create(orden=orden, receta=item['receta'], precio_receta=item['precio_receta'], cantidad=item['cantidad'])
            cart.clear()
            return render(request, 'cliente/paypal/paypal.html', {'order': orden})
    else:
        form = OrderCreateForm()
    return render(request, 'cliente/orden_compra/crear_orden.html', {'cart': cart, 'form': form})



def agregar_producto(request, receta_id):
    cart = Cart(request)
    receta = Receta.objects.get(id=receta_id)
    cart.add(receta)
    return redirect("cliente:pedir")


def eliminar_producto(request, receta_id):
    cart = Cart(request)
    receta = Receta.objects.get(id=receta_id)
    cart.remove(receta)
    return redirect("cliente:pedir")


def restar_producto(request, receta_id):
    cart = Cart(request)
    receta = Receta.objects.get(id=receta_id)
    cart.decrement(receta)
    return redirect("cliente:pedir")


def limpiar_carrito(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cliente:pedir")



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------



class CrearOrden(CreateView): # Crear Reserva
    model = OrdenCompra
    form_class = OrderCreateForm
    template_name = 'cliente/orden_compra/crear_orden.html'
    success_url = reverse_lazy('cliente:pagar')



def pago_paypal(request):
    return render(request, template_name= 'cliente/paypal/paypal.html')



class Gracias(TemplateView):
    template_name = 'cliente/orden_compra/gracias.html'



# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------







# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

class InicioCliente(TemplateView):
    template_name = 'cliente/area_cliente/index_cliente.html'
    
class CodigoReserva(TemplateView):
    template_name = 'cliente/area_cliente/codigo_reserva.html'
    
class Menu(TemplateView):
    template_name = 'cliente/area_cliente/menu.html'



# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------



class ListadoReserva(View): # Listado de Reservas
    model = Reserva
    form_class = ReservaForm
    template_name = 'cliente/listar_reserva.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['reservas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        
        

class CrearReserva(CreateView): # Crear Reserva
    model = Reserva
    form_class = ReservaForm
    template_name = 'cliente/crear_reserva.html'
    success_url = reverse_lazy('cliente:listado_reservas')


class EliminarReserva(DeleteView): #Eliminar Reserva 
    model = Reserva
    success_url = reverse_lazy('cliente:listado_reservas')



# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------



class ListadoBoleta(View): # Listado de Boletas
    model = OrdenCompra
    form_class = OrderCreateForm
    template_name = 'cliente/boleta/emitir_boleta.html'  
    
    def get_queryset(self):
        return self.model.objects.filter()
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['ordenes'] = self.get_queryset()
        contexto['form'] = self.form_class()
        return contexto
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
        


# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------