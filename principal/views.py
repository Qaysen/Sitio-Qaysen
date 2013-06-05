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
