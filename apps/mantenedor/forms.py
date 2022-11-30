from socket import fromshare
from django import forms
from .models import Producto, Proveedor, Mesa, Receta, Bodega

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'cantidad', 'proveedor', 'descripcion']
        labels = {
            'nombre_producto': 'Nombre del producto',
            'cantidad': 'Cantidad de unidades del producto',
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
            'proveedor': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del proveedor del producto',
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
 

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
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


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


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


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre_receta', 'precio_receta', 'image', 'tiempo_preparacion')
        label = {
            'nombre_receta':'Nombre de la receta',
            'precio_receta':'Precio de la receta',
            'image':'Imagen de la receta',
            'tiempo_preparacion':'Tiempo de preparación aprox.',
        }
        widgets = {
            'nombre_receta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el nombre de la receta o bebestible'
                }
            ),
            'precio_receta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el precio de la receta o bebestible'
                }
            ),
            'tiempo_preparacion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese el tiempo aprox. de preparación de la receta'
                }
            ),
        }


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ('proveedor', 'productos', 'cantidad')
        label = {
            'proveedor':'Proveedor',
            'productos':'Productos',
            'cantidad':'Cantidad',
        }
        widgets = {
            'proveedor':forms.Select(
            attrs={
                'class':'form-control',
                'placeholder':'Selecciona el Proveedor'
            }
            ),
            'productos':forms.Select(
            attrs={
                'class':'form-control' ,
                'placeholder':'Selecciona el Producto'
            }
            ),
            'cantidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': ' Ingrese la Cantidad'
                }
            ),
        }