from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	# 
    url(r'^$', 'principal.views.inicio'),
    url(r'^nosotros/$', 'principal.views.nosotros'),
    url(r'^contactanos/$', 'principal.views.contacto'),

    url(r'^servicios/$', 'principal.views.ver_servicios'),    
    url(r'^servicios/(?P<nomservicio>[-\w]+)/$','principal.views.detalleservicio'),
    url(r'^productos/$', 'principal.views.ver_productos'),
    url(r'^productos/(?P<nomproducto>[-\w]+)/$','principal.views.detalleproducto'),
    url(r'^clientes/$','principal.views.cliente'),
    url(r'^proyectos/$','principal.views.proyecto'),

   )
