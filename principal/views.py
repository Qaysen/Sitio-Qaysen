from principal.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import ContactoForm
from django.core.mail import EmailMultiAlternatives #ENVIAR HTML
# Pagina de inicio
def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario=ContactoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			to_admin='edulozano.30@gmail.com'
			html_contenido = "<p>Preguntas o Inquietudes del Cliente :</p><br><br><b>Nombre de la persona que envia: </b> %s <br><b>email: </b> %s<br><b>Descripcion:</b> %s  "%(request.POST['nombre'] ,request.POST['e_mail'],request.POST['descripcion'])
			msg = EmailMultiAlternatives('Solicitar Informacion de Qaysen Sac',html_contenido,'from@server.com',[to_admin])
			msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
			msg.send()
			return HttpResponseRedirect('/')
	else:
		formulario=ContactoForm()
	return render_to_response('contacto.html', {'formulario':formulario},context_instance=RequestContext(request))


def nosotros(request):
	nosotros=Nosotros.objects.all()
	equipo=Equipo.objects.all().order_by('?')
	return render_to_response('nosotros.html', {'nosotros':nosotros,'equipo':equipo},context_instance=RequestContext(request))

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