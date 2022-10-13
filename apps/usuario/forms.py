from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        

class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos """
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
    ))
    
    password2 = forms.CharField(label = 'Contraseña de confirmación', widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id':'password2',
            'required':'required',
            }
    ))
    
    class Meta:
        model=Usuario
        fields=('email','username','nombres','apellidos','rol')
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electrónico',
                }
            ),
            'nombres':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                }
            ),
            'rol':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
        }
        

    def clean_password2(self):
        """ Esta es la validación de la contraseña
            Este método valida que las contraseñas sean iguales, esto antes de ser encriptadas y guardadas
            en la base de datos, Retornar la contraseña válida.
            Cuando las contraseñas no son iguales muestra un mensaje de error."""
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
        
        
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user