#encoding:utf-8

from principal.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import ContactoForm, SuscripcionForm
from random import choice
from django.core.mail import EmailMultiAlternatives #ENVIAR HTML
from django.utils import simplejson as json
# Pagina de inicio
def inicio(request):
	slider =Slider.objects.all()
	productos=Producto.objects.order_by('?')[:4]
	servicios=Servicio.objects.order_by('?')[:4]
	return render_to_response('inicio2.html', {'slider':slider,'productos':productos,'servicios':servicios},context_instance=RequestContext(request))

def coordenadas_mapa(request):
	if request.is_ajax():
		ubicacion_id=1
		info=InfContacto.objects.get(pk=ubicacion_id) 
		data=json.dumps({'latitud':float(info.latitud),'longitud':float(info.longitud)})
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404


def contacto(request):
	info=InfContacto.objects.get(pk=1)
	if request.method=='POST':
		formulario=ContactoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			to_admin='elicia.cor@gmail.com'
			html_contenido = "<p>Preguntas o Inquietudes del Cliente :</p><br><br><b>Nombre de la persona que envia: </b> %s <br>Ciudad: </br> %s <br><b>email: </b> %s <br>Telefono: </br> %s <br><b>Comentario: </b> %s  "%(request.POST['nombre'] , request.POST['ciudad'] ,request.POST['e_mail'],request.POST['telefono'] ,request.POST['comentario'])
			msg = EmailMultiAlternatives('Solicitar Informacion',html_contenido,'from@server.com',[to_admin])
			msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
			msg.send()
			return HttpResponseRedirect('/')
	else:
		formulario=ContactoForm()
	return render_to_response('contacto.html', {'formulario':formulario,'info':info},context_instance=RequestContext(request))


def nosotros(request):
	nosotros=Nosotros.objects.all()
	equipo=Equipo.objects.all().order_by('?')
	return render_to_response('nosotros.html', {'nosotros':nosotros,'equipo':equipo},context_instance=RequestContext(request))


def ver_servicios(request):
	servicios=Servicio.objects.all().order_by('?')		
	return render_to_response('servicios.html', {'servicios':servicios},context_instance=RequestContext(request))

def detalleservicio(request, nomservicio):
	servicio=Servicio.objects.get(slug=nomservicio)	
	if servicio.tipo == "Conplan":
		planes=Plan.objects.filter(servicio=servicio.id)
		return render_to_response('detalle_servicio_cp.html',{'servicio':servicio, 'planes':planes},context_instance = RequestContext(request))
	else:
		caracteristicas=ServicioCaract.objects.filter(servicio=servicio.id)
		print caracteristicas
		return render_to_response('detalle_servicio_sp.html',{'servicio':servicio,'caracteristicas':caracteristicas},context_instance = RequestContext(request))


def ver_productos(request):
	productos=Producto.objects.all().order_by('?')	
	return render_to_response('productos.html', {'productos':productos},context_instance=RequestContext(request))


def detalleproducto(request, nomproducto):
	producto=Producto.objects.get(slug=nomproducto)
	return render_to_response('detalle_producto.html',{'producto':producto},context_instance = RequestContext(request))

def cliente(request):
	clientes = Cliente.objects.all()
	return render_to_response('cliente.html',{'clientes':clientes},context_instance=RequestContext(request))

def proyecto(request):
	imagenes=ImgProyecto.objects.all()
	ims= imagenes.values('proyecto__id','proyecto__nombre','proyecto__descripcion').distinct()
	mis_proyectos=[]
	for indice,elemento in enumerate(ims):
		x=imagenes.filter(proyecto__id=elemento['proyecto__id'])
		mis_proyectos.append({
			'nombre':elemento['proyecto__nombre'],
			'descripcion':elemento['proyecto__descripcion'],
			'imagen':x[0].img			
			})
	return render_to_response('proyecto.html',{'proyectos':mis_proyectos},context_instance=RequestContext(request))

def suscripcion(request):
	if request.method=='POST':
		formu= request.POST.copy()
		codigo = make_random_password()
		formu['codigo']= codigo
		formulario=SuscripcionForm(formu)
		if formulario.is_valid():
			formulario.save()
			html_contenido ="<p>Usted ha sido suscrito a nuetras novedades de productos y servicios :</p><br><br>"
			html_contenido+="<b>Su email: </b> %s </b>"%(request.POST['email'])
			html_contenido+="<br>Si no desea recibir mas informacion, por favor de clic" 
			html_contenido+="<br><a title='Cancelar la suscripcion de esta web' href='http://wwww.qaysen.com/suscripcion/salir/%s'>AQUI</a>"%(codigo)
			msg = EmailMultiAlternatives('suscripción  a Qaysen S.A.C',html_contenido ,'from@server.com',[request.POST['email']])
			msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
			msg.send()
			return HttpResponseRedirect('/suscripcion')
	else:
		formulario=SuscripcionForm()
	return render_to_response('suscripcion.html', {'formulario':formulario},context_instance=RequestContext(request))

def make_random_password(length=40, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
	return ''.join([choice(allowed_chars) for i in range(length)])


def salir_suscripcion(request,codigo):
	codigo =Suscripcion.objects.get(codigo=codigo)
	if request.method=='POST':
		codigo.delete()
	return render_to_response('salir_suscripcion.html', {'email':codigo},context_instance=RequestContext(request))
