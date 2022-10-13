from socket import fromshare
from django import forms
from .models import Autor, Libro, Mesa, Receta

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre_producto', 'cantidad', 'precio', 'proveedor', 'descripcion']
        labels = {
            'nombre_producto': 'Nombre del producto',
            'cantidad': 'Cantidad de unidades del producto',
            'precio': 'Precio del producto',
            'proveedor': 'Proveedor del producto',
            'descripcion': 'Pequeña descripción',
        }
        widgets = {
            'nombre_producto': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del producto',
                    'id':'nombre_producto',
                }
            ),
            'cantidad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la cantidad',
                    'id':'cantidad',
                }
            ),
            'precio': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio del producto',
                    'id':'precio',
                }
            ),
            'proveedor': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del proveedor del producto',
                    'id':'proveedor',
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una pequeña descripción para el producto',
                    'id':'descripcion'
                }
            ), 
        }
        



class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('nombre_proveedor', 'correo_proveedor', 'telefono_proveedor')
        label = {
            'nombre_proveedor':'Nombre del proveedor',
            'correo_proveedor':'Correo del proveedor',
            'telefono_proveedor':'Teléfono del proveedor',
        }
        widgets = {
            'nombre_proveedor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese nombre del proveedor'
                }
            ),
            'correo_proveedor': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese correo del proveedor'
                }
            ),
            'telefono_proveedor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese número de teléfono del proveedor'
                }
            ),
            
            # 'autor_id': forms.SelectMultiple(
            #     attrs = {
            #         'class':'form-control'
            #     }
            # ),
            # 'fecha_publicacion': forms.SelectDateWidget(
            #     attrs = {
            #         'class': 'form-control'
            #     }
            # )
        }





class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ('numero_mesa', 'descripcion_mesa', 'cantidad_personas')
        label = {
            'numero_mesa':'Número de la mesa',
            'descripcion_mesa':'Descripción mesa',
            'cantidad_personas':'Cantidad de personas',
        }
        widgets = {
            'numero_mesa': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el número que le asignará a la mesa'
                }
            ),
            'descripcion_mesa': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese una descripción para la mesa'
                }
            ),
            'cantidad_personas': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el máximo de personas que se pueden sentar en la mesa'
                }
            ),
        }





class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre_receta', 'precio_receta', 'tiempo_preparacion')
        label = {
            'nombre_receta':'Nombre de la receta',
            'precio_receta':'Precio de la receta',
            'tiempo_preparacion':'Tiempo de preparación aprox.',
        }
        widgets = {
            'nombre_receta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el nombre de la receta'
                }
            ),
            'precio_receta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el precio que va a costar'
                }
            ),
            'tiempo_preparacion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el tiempo aprox. de preparación de la receta'
                }
            ),
        }