from socket import fromshare
from django import forms
from .models import Reserva,Boleta,OrdenCompra

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['email_cliente', 'nombre_cliente', 'apellido_cliente', 'telefono_cliente', 
                  'fecha_reserva', 'hora_reserva', 'numero_mesa']
        labels = {
            'email_cliente': 'Correo electrónico del cliente',
            'nombre_cliente': 'Nombre del cliente',
            'apellido_cliente': 'Apellido del cliente',
            'telefono_cliente': 'Número de teléfono del cliente',
            'fecha_reserva': 'Día de la reserva',
            'hora_reserva': 'Hora de la reserva',
            'numero_mesa': 'Elija la mesa que desea reservar',
        }
        widgets = {
            'email_cliente': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese correo del cliente'
                }
            ),
            'nombre_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese nombre del cliente'
                }
            ),
            'apellido_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese apellido del cliente'
                }
            ),
            'telefono_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese número de teléfono del cliente'
                }
            ),
            'fecha_reserva': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'hora_reserva': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'numero_mesa': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }




class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['nombre_apellido_cliente', 'total_a_pagar', 'fecha_de_pago', 'estado', ]
        labels = {
            'nombre_apellido_cliente': 'Nombre y apellido del cliente',
            'total_a_pagar': 'Total a pagar',
            'fecha_de_pago': 'Fecha de pago',
            'estado': 'Estado',
        }
        widgets = {
            'nombre_apellido_cliente': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Seleccione el nombre del cliente'
                }
            ),
            'total_a_pagar': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el total a pagar'
                }
            ),
            'fecha_de_pago': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese la fecha de pago'
                }
            ),
            'estado': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Seleccione el estado de la boleta'
                }
            ),
        }
        
        
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        fields = ['nombre_cliente', 'apellido_cliente', 'email_cliente',]
        labels = {
            'nombre_cliente': 'Nombre del cliente',
            'apellido_cliente': 'Apellido del cliente',
            'email_cliente': 'Email del cliente',
        }
        widgets = {
            'nombre_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'apellido_cliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido'
                }
            ),
            'email_cliente': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese su email'
                }
            ),
        }
