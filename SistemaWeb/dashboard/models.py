from decimal import Decimal
import decimal
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username.capitalize()
    

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    celular = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    atencion = models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)
    ruc_dni = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=200)
    obs= models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.cliente
    def get_direcciones(self):
        return self.direccion_set.all()
class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.direccion

class Moneda(models.Model):
    tipo = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.tipo

class Pago(models.Model):
    condicion = models.CharField(max_length=20)
    def __str__(self):
        return self.condicion
class Bu(models.Model):
    bu=models.CharField(max_length=200)
    def __str__(self):
        return self.bu
    
def generar_nombre_proforma(instance):
    year = instance.fecha.year % 100
    month = instance.fecha.month
    return f"Proforma {instance.id}-OPDM{year}.{month}"

class Proforma(models.Model):
    fecha = models.DateField(auto_now=True)
    bu = models.ForeignKey(Bu, on_delete=models.CASCADE)
    condicion_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    validez = models.CharField(max_length=20)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    correo = models.CharField(max_length=200, blank=True)
    celular = models.CharField(max_length=9, blank=True)
    actividad = models.CharField(max_length=500, blank=True)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        year = self.fecha.year % 100
        month = self.fecha.month
        return f"Proforma {self.id}-OPDM{year}.{month}"

class ProformaConsultoria(models.Model):
    fecha = models.DateField(auto_now=True)
    bu = models.ForeignKey(Bu, on_delete=models.CASCADE)
    condicion_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    validez = models.CharField(max_length=20)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    correo = models.CharField(max_length=200, blank=True)
    celular = models.CharField(max_length=9, blank=True)
    actividad = models.CharField(max_length=500, blank=True)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        year = self.fecha.year % 100
        month = self.fecha.month
        return f"Proforma {self.id}-OPC{year}.{month}"  

class ProformaManoDeObra(models.Model):
    fecha = models.DateField(auto_now=True)
    bu = models.ForeignKey(Bu, on_delete=models.CASCADE)
    condicion_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    validez = models.CharField(max_length=20)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    correo = models.CharField(max_length=200, blank=True)
    celular = models.CharField(max_length=9, blank=True)
    actividad = models.CharField(max_length=500, blank=True)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        year = self.fecha.year % 100
        month = self.fecha.month
        return f"Proforma {self.id}-OPDMO{year}.{month}" 



class Cotizacion(models.Model):
    proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return f" {self.proforma} del cliente {self.cliente}"
    
class CotizacionConsultoria(models.Model):
    proforma = models.ForeignKey(ProformaConsultoria, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return f" {self.proforma} del cliente {self.cliente}"
    
class CotizacionManoDeObra(models.Model):
    proforma = models.ForeignKey(ProformaManoDeObra, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return f" {self.proforma} del cliente {self.cliente}"


class piezasRepuesto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    marca =models.CharField(max_length=100,blank=True)
    observacion = models.CharField(max_length=200 , blank=True)
    imagen_tienda = models.ImageField(upload_to='imgPiezas', null=True , blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,default=0,blank=True)
    tipo_moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE, blank=True,null=True)
    peso=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.codigo
    
class Consultoria(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True , blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,default=0,blank=True)

    def __str__(self):
        return self.codigo
    
class ManodeObra(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200,null=True , blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,default=0,blank=True)
    tipo_moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.codigo

class descripcionCotizacion(models.Model):
    DESCUENTO_CHOICES = (
        (0, 'Sin descuento'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
    )
    DESCUENTO_TIPO_CHOICES = (
        ('porcentaje', 'Porcentaje'),
        ('manual', 'Manual'),
    )
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    codigo = models.ForeignKey(piezasRepuesto,on_delete=models.CASCADE,null=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    disponibilidad = models.CharField(max_length=20)
    precio_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    descuento_tipo = models.CharField(max_length=10, choices=DESCUENTO_TIPO_CHOICES, default='porcentaje')
    descuento = models.IntegerField(choices=DESCUENTO_CHOICES,  default=0)
    descuento_manual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



    def __str__(self):
        return f"Cotizacion{self.cotizacion}"
    
class descripcionCotizacionConsultoria(models.Model):
    DESCUENTO_CHOICES = (
        (0, 'Sin descuento'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
    )
    DESCUENTO_TIPO_CHOICES = (
        ('porcentaje', 'Porcentaje'),
        ('manual', 'Manual'),
    )
    cotizacion = models.ForeignKey(CotizacionConsultoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    codigo = models.ForeignKey(Consultoria,on_delete=models.CASCADE,null=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    precio_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    descuento_tipo = models.CharField(max_length=10, choices=DESCUENTO_TIPO_CHOICES, default='porcentaje')
    descuento = models.IntegerField(choices=DESCUENTO_CHOICES,  default=0)
    descuento_manual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"Cotizacion{self.cotizacion}"
    
class descripcionCotizacionManoDeObra(models.Model):
    DESCUENTO_CHOICES = (
        (0, 'Sin descuento'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
    )
    DESCUENTO_TIPO_CHOICES = (
        ('porcentaje', 'Porcentaje'),
        ('manual', 'Manual'),
    )
    cotizacion = models.ForeignKey(CotizacionManoDeObra, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    codigo = models.ForeignKey(ManodeObra,on_delete=models.CASCADE,null=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    precio_total = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    descuento_tipo = models.CharField(max_length=10, choices=DESCUENTO_TIPO_CHOICES, default='porcentaje')
    descuento = models.IntegerField(choices=DESCUENTO_CHOICES,  default=0)
    descuento_manual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"Cotizacion{self.cotizacion}"


#Signals 

# Señal para actualizar campos de correo y celular al agregar o editar una ProformaConsultoria
@receiver([post_save, pre_save], sender=ProformaManoDeObra)
def update_vendedor_info_obra(sender, instance, **kwargs):
    if instance.vendedor:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.vendedor != instance.vendedor or not instance.pk:
                instance.correo = instance.vendedor.correo
                instance.celular = instance.vendedor.celular
            else:
                instance.correo = old_instance.correo
                instance.celular = old_instance.celular
        except sender.DoesNotExist:
            instance.correo = instance.vendedor.correo
            instance.celular = instance.vendedor.celular

# Señal para actualizar campos de correo y celular al agregar o editar una ProformaConsultoria
@receiver([post_save, pre_save], sender=ProformaConsultoria)
def update_vendedor_info_consultoria(sender, instance, **kwargs):
    if instance.vendedor:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.vendedor != instance.vendedor or not instance.pk:
                instance.correo = instance.vendedor.correo
                instance.celular = instance.vendedor.celular
            else:
                instance.correo = old_instance.correo
                instance.celular = old_instance.celular
        except sender.DoesNotExist:
            instance.correo = instance.vendedor.correo
            instance.celular = instance.vendedor.celular

# Señal para actualizar campos de correo y celular al agregar o editar una Proforma
@receiver([post_save, pre_save], sender=Proforma)
def update_vendedor_info_proforma(sender, instance, **kwargs):
    if instance.vendedor:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.vendedor != instance.vendedor or not instance.pk:
                instance.correo = instance.vendedor.correo
                instance.celular = instance.vendedor.celular
            else:
                instance.correo = old_instance.correo
                instance.celular = old_instance.celular
        except sender.DoesNotExist:
            instance.correo = instance.vendedor.correo
            instance.celular = instance.vendedor.celular


@receiver(post_save, sender=descripcionCotizacion)
def update_descripcionCotizacion_info(sender, instance, **kwargs):
    nombre_repuesto = instance.codigo
    if nombre_repuesto:
        instance.descripcion = nombre_repuesto.nombre
        instance.precio_unitario = nombre_repuesto.precio_unitario
        return instance.precio_unitario



@receiver(pre_save, sender=descripcionCotizacion)
def update_precio_total(sender, instance, **kwargs):
    if instance.cantidad is not None and instance.precio_unitario is not None:
        try:
            precio_unitario_decimal = Decimal(instance.precio_unitario)
        except (decimal.InvalidOperation, TypeError, ValueError):
            precio_unitario_decimal = Decimal('0')
        if instance.descuento_tipo == 'porcentaje':
            descuento_decimal = Decimal(instance.descuento) / Decimal('100') if instance.descuento is not None else Decimal('0')
            precio_unitario_descuento = precio_unitario_decimal * (1 - descuento_decimal)
            instance.precio_total = instance.cantidad * precio_unitario_descuento
        elif instance.descuento_tipo == 'manual':
            instance.precio_total = instance.cantidad * precio_unitario_decimal
            # Si el descuento es manual, aplicar el descuento directamente al precio unitario
            descuento_decimal = Decimal(instance.descuento_manual) if instance.descuento_manual is not None else Decimal('0')
            instance.precio_total = instance.precio_total - descuento_decimal

@receiver(post_save, sender=descripcionCotizacionConsultoria)
def update_descripcionCotizacion_info_consultoria(sender, instance, **kwargs):
    nombre_repuesto = instance.codigo
    if nombre_repuesto:
        instance.descripcion = nombre_repuesto.nombre
        instance.precio_unitario = nombre_repuesto.precio_unitario
        return instance.precio_unitario



@receiver(pre_save, sender=descripcionCotizacionConsultoria)
def update_precio_total_consultoria(sender, instance, **kwargs):
    if instance.cantidad is not None and instance.precio_unitario is not None:
        try:
            precio_unitario_decimal = Decimal(instance.precio_unitario)
        except (decimal.InvalidOperation, TypeError, ValueError):
            precio_unitario_decimal = Decimal('0')
        if instance.descuento_tipo == 'porcentaje':
            descuento_decimal = Decimal(instance.descuento) / Decimal('100') if instance.descuento is not None else Decimal('0')
            precio_unitario_descuento = precio_unitario_decimal * (1 - descuento_decimal)
        else:
            descuento_decimal = Decimal(instance.descuento_manual)
            precio_unitario_descuento = precio_unitario_decimal - descuento_decimal
        instance.precio_total = instance.cantidad * precio_unitario_descuento

@receiver(post_save, sender=descripcionCotizacionManoDeObra)
def update_descripcionCotizacion_info_obra(sender, instance, **kwargs):
    nombre_repuesto = instance.codigo
    if nombre_repuesto:
        instance.descripcion = nombre_repuesto.nombre
        instance.precio_unitario = nombre_repuesto.precio_unitario
        return instance.precio_unitario



@receiver(pre_save, sender=descripcionCotizacionManoDeObra)
def update_precio_total_obra(sender, instance, **kwargs):
    if instance.cantidad is not None and instance.precio_unitario is not None:
        try:
            precio_unitario_decimal = Decimal(instance.precio_unitario)
        except (decimal.InvalidOperation, TypeError, ValueError):
            precio_unitario_decimal = Decimal('0')
        if instance.descuento_tipo == 'porcentaje':
            descuento_decimal = Decimal(instance.descuento) / Decimal('100') if instance.descuento is not None else Decimal('0')
            precio_unitario_descuento = precio_unitario_decimal * (1 - descuento_decimal)
        else:
            descuento_decimal = Decimal(instance.descuento_manual)
            precio_unitario_descuento = precio_unitario_decimal - descuento_decimal
        instance.precio_total = instance.cantidad * precio_unitario_descuento




