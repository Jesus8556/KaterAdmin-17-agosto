from datetime import date
import datetime
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_select2 import forms as s2forms


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'


class MonedaForm(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = '__all__'


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'


class BuForm(forms.ModelForm):
    class Meta:
        model = Bu
        fields = '__all__'


class ProformaForm(forms.ModelForm):
    class Meta:
        model = Proforma
        fields = '__all__'

    fecha = forms.DateField(
        label='Fecha O/P', widget=forms.DateInput(attrs={'type': 'date'}))

    # Añadimos los campos de correo y celular como no requeridos y ocultos
    correo = forms.EmailField(required=False, widget=forms.HiddenInput())
    celular = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si el formulario no tiene una instancia (es decir, es para agregar una nueva proforma),
        # configuramos el valor del campo fecha en la fecha actual
        if not self.instance.pk:
            self.initial['fecha'] = date.today()

    def clean_fecha(self):
        # Si se seleccionó "Hoy", establecer la fecha actual en el campo de fecha
        fecha = self.cleaned_data['fecha']
        if fecha == date.today():
            return date.today()
        return fecha
    
    def save(self, commit=True):
        instance = super().save(commit=commit)
        year = instance.fecha.year % 100
        month = instance.fecha.month
        instance.__str__ = lambda: f"Proforma {instance.id}-OPDM{year}.{month}"
        if commit:
            instance.save()
        return instance

class ProformaConsultoriaForm(forms.ModelForm):
    class Meta:
        model = ProformaConsultoria
        fields = '__all__'

    fecha = forms.DateField(
        label='Fecha O/P', widget=forms.DateInput(attrs={'type': 'date'}))

    # Añadimos los campos de correo y celular como no requeridos y ocultos
    correo = forms.EmailField(required=False, widget=forms.HiddenInput())
    celular = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si el formulario no tiene una instancia (es decir, es para agregar una nueva proforma),
        # configuramos el valor del campo fecha en la fecha actual
        if not self.instance.pk:
            self.initial['fecha'] = date.today()

    def clean_fecha(self):
        # Si se seleccionó "Hoy", establecer la fecha actual en el campo de fecha
        fecha = self.cleaned_data['fecha']
        if fecha == date.today():
            return date.today()
        return fecha

class ProformaManoDeObraForm(forms.ModelForm):
    class Meta:
        model = ProformaManoDeObra
        fields = '__all__'

    fecha = forms.DateField(
        label='Fecha O/P', widget=forms.DateInput(attrs={'type': 'date'}))

    # Añadimos los campos de correo y celular como no requeridos y ocultos
    correo = forms.EmailField(required=False, widget=forms.HiddenInput())
    celular = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si el formulario no tiene una instancia (es decir, es para agregar una nueva proforma),
        # configuramos el valor del campo fecha en la fecha actual
        if not self.instance.pk:
            self.initial['fecha'] = date.today()

    def clean_fecha(self):
        # Si se seleccionó "Hoy", establecer la fecha actual en el campo de fecha
        fecha = self.cleaned_data['fecha']
        if fecha == date.today():
            return date.today()
        return fecha

    def save(self, commit=True):
        instance = super().save(commit=commit)
        year = instance.fecha.year % 100
        month = instance.fecha.month
        instance.__str__ = lambda: f"Proforma {instance.id}-OPMDO{year}.{month}"
        if commit:
            instance.save()
        return instance
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        
class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['proforma', 'cliente','observacion']
        widgets = {
            'proforma': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class CotizacionConsultoriaForm(forms.ModelForm):
    class Meta:
        model = CotizacionConsultoria
        fields = ['proforma', 'cliente','observacion']
        widgets = {
            'proforma': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class CotizacionManoDeObraForm(forms.ModelForm):
    class Meta:
        model = CotizacionManoDeObra
        fields = ['proforma', 'cliente','observacion']
        widgets = {
            'proforma': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class PiezasRepuestoForm(forms.ModelForm):
    class Meta:
        model = piezasRepuesto
        fields = '__all__'

class descripcionWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "codigo__icontains"
    ]
    def label_from_instance(self, obj):
        return obj.codigo
    
class DescripcionCotizacionForm(forms.ModelForm):
    class Meta:
       
        model = descripcionCotizacion
        fields = '__all__'
        widgets = {
            'cotizacion': forms.HiddenInput(),
            'codigo': descripcionWidget,
            'descripcion' :forms.HiddenInput(),
            'descuento_tipo': forms.RadioSelect(choices=descripcionCotizacion.DESCUENTO_TIPO_CHOICES,),
            'precio_unitario': forms.HiddenInput(),
            'precio_total': forms.HiddenInput(),
            'descuento': forms.Select(attrs={'required': 'required'}),
        }

class descripcionWidgetConsultoria(s2forms.ModelSelect2Widget):
    search_fields = [
        "codigo__icontains"
    ]
    def label_from_instance(self, obj):
        return obj.codigo
    
class DescripcionCotizacionConsultoriaForm(forms.ModelForm):
    class Meta:
        model = descripcionCotizacionConsultoria
        fields = '__all__'
        widgets = {
            'cotizacion': forms.HiddenInput(),
            'codigo': descripcionWidgetConsultoria,
            'descripcion' :forms.HiddenInput(),
            'descuento_tipo': forms.RadioSelect(choices=descripcionCotizacion.DESCUENTO_TIPO_CHOICES,),
            'precio_unitario': forms.HiddenInput(),
            'precio_total': forms.HiddenInput(),
            'descuento': forms.Select(attrs={'required': 'required'}),
        }

class descripcionWidgetManoDeObra(s2forms.ModelSelect2Widget):
    search_fields = [
        "codigo__icontains"
    ]
    def label_from_instance(self, obj):
        return obj.codigo
class DescripcionCotizacionManoDeObraForm(forms.ModelForm):
    class Meta:
        model = descripcionCotizacionManoDeObra
        fields = '__all__'
        widgets = {
            'cotizacion': forms.HiddenInput(),
            'codigo': descripcionWidgetManoDeObra,
            'descripcion' :forms.HiddenInput(),
            'descuento_tipo': forms.RadioSelect(choices=descripcionCotizacion.DESCUENTO_TIPO_CHOICES,),
            'precio_unitario': forms.HiddenInput(),
            'precio_total': forms.HiddenInput(),
            'descuento': forms.Select(attrs={'required': 'required'}),
        }
    


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = piezasRepuesto
        fields = '__all__'

class ConsultoriaForm(forms.ModelForm):
    class Meta:
        model = Consultoria
        fields = '__all__'

class ManoDeObraForm(forms.ModelForm):
    class Meta:
        model = ManodeObra
        fields = '__all__'


class CambiarMonedaForm(forms.Form):
    nueva_moneda = forms.ModelChoiceField(
        queryset=Moneda.objects.all(),
        label="Cambiar moneda",
        required=False,
        empty_label="Seleccione una moneda"
    )