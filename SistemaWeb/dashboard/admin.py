from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Moneda)
admin.site.register(Pago)
admin.site.register(Proforma)
admin.site.register(Bu)
admin.site.register(Cotizacion)
admin.site.register(piezasRepuesto)
admin.site.register(descripcionCotizacion)
admin.site.register(Consultoria)
admin.site.register(ManodeObra)
admin.site.register(ProformaConsultoria)
admin.site.register(ProformaManoDeObra)
