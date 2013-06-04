from principal.models import *
from django.contrib import admin


class AdminEntries(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['nombre'] }

admin.site.register(Equipo)
admin.site.register(Nosotros)
admin.site.register(InfContacto)
admin.site.register(Contactenos)
admin.site.register(Slider)
admin.site.register(Cliente)
admin.site.register(Servicios, AdminEntries)
admin.site.register(Proyecto, AdminEntries)
admin.site.register(ImgProyecto)
admin.site.register(RespSocial, AdminEntries)
admin.site.register(ImgRespSocial)
admin.site.register(DetalleProducto)
admin.site.register(Producto, AdminEntries)
admin.site.register(Evento, AdminEntries)


