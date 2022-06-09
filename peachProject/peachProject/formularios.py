from django import forms
from peach.models import *

tipo_servicios = TipoServicio.objects.all()

choices_servicios=[]
for item in tipo_servicios:
    choices_servicios.append((item.id,item.nombre))
choices_servicios= tuple(choices_servicios)

estado_encuestas = Estado.objects.all()

choices_encuestas=[]
for item in estado_encuestas:
    choices_encuestas.append((item.id,item.estado))
choices_encuestas= tuple(choices_encuestas)


class ServicioFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.Textarea())
    descripcion = forms.CharField(max_length=250, widget=forms.Textarea())
    costo = forms.FloatField()
    Tipo = forms.ChoiceField(choices=choices_servicios)

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        '''widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'lol'})
        }'''
        '''def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['fecha'].widget.attrs['placeholder'] = self.fields['fecha'].label or 'yyyy-mm-dd' '''


class EncuestaFormulario(forms.Form):
    ocupacion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'ejm. Ingeniero'}))
    experiencia = forms.IntegerField(min_value=1, max_value=30,  widget=forms.NumberInput())
    estado = forms.ChoiceField(choices=choices_encuestas)

class ContactoFormulario(forms.Form):
    nombres= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}))
    apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}))
    empresa = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese donde trabaja'}))
    descripcion = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'placeholder': 'Ingrese descripcion de la empresa'}))
    direccion= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Direccion de empresa'}))
    telefono= forms.CharField(min_length=10, max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su telefono'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com'}))
    interes = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Ingrese su interes en nuestros servicios'}))