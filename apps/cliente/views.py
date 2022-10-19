from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from apps.cliente.models import Reserva
from apps.cliente.forms import ReservaForm

# Create your views here.


class InicioCliente(TemplateView):
    template_name = 'cliente/index_cliente.html'
    
class CodigoReserva(TemplateView):
    template_name = 'cliente/codigo_reserva.html'


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