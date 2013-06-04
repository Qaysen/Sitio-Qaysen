from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


GENERO = (
	('Masculino','Masculino'),
	('Femenino','Femenino')
)

class Equipo(models.Model):
	usuario = models.ForeignKey(User)	
	descripcion = models.CharField(max_length=500)
	cargo=models.CharField(max_length=20)
	img=models.FileField(upload_to='fotoCarnet/')
	genero = models.CharField(null=True,blank=True,choices=GENERO,max_length=30)
	direccion= models.CharField(null=True,blank=True,max_length=300)
	telefono= models.CharField(null=True,blank=True,max_length=10)
	git= models.CharField(null=True,blank=True,max_length=100)
	face = models.CharField(null=True,blank=True,max_length=100)
	twitter = models.CharField(null=True,blank=True,max_length=100)
	linkedin = models.CharField(null=True,blank=True,max_length=100)
	def __unicode__(self):
		return unicode(self.usuario)

class Nosotros(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)

	def __unicode__(self):
		return self.titulo

class InfContacto(models.Model):	
	mapa = models.CharField(max_length=100)
	e_mail = models.EmailField(max_length=50)	
	direccion= models.CharField(null=True,blank=True,max_length=300)
	telefono= models.CharField(null=True,blank=True,max_length=10)
	cell= models.CharField(null=True,blank=True,max_length=9)
	ruc= models.CharField(null=True,blank=True,max_length=10)
	git= models.CharField(null=True,blank=True,max_length=100)
	face = models.CharField(null=True,blank=True,max_length=100)
	twitter = models.CharField(null=True,blank=True,max_length=100)
	google= models.CharField(null=True,blank=True,max_length=100)
	

	def __unicode__(self):
		return self.mapa

class Contactenos(models.Model):	
	nombre = models.CharField(max_length=100)
	e_mail = models.EmailField(max_length=50)
	descripcion = models.TextField()	

	def __unicode__(self):
		return self.nombre

class Slider(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	img=models.FileField(upload_to='imgSlider/')	

	def __unicode__(self):
		return self.titulo	


class Cliente(models.Model):
	nombre = models.CharField(max_length=100)	
	direccion= models.CharField(null=True,blank=True,max_length=300)
	telefono= models.CharField(null=True,blank=True,max_length=10)
	razonSocial = models.CharField(max_length=100)
	logo=models.FileField(upload_to='logoCliente/')
	

	def __unicode__(self):
		return self.nombre

class Servicios(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	img=models.FileField(upload_to='imgServicios/')
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Servicios, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)	
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Proyecto, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class ImgProyecto(models.Model):
	proyecto = models.ForeignKey(Proyecto)	
	descripcion= models.CharField(null=True,blank=True,max_length=300)
	titulo= models.CharField(null=True,blank=True,max_length=10)	
	img=models.FileField(upload_to='imgProyecto/')
	

	def __unicode__(self):
		return self.titulo

class RespSocial(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	fecha=models.DateField(auto_now=False)
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(RespSocial, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class ImgRespSocial(models.Model):
	respSocial = models.ForeignKey(RespSocial)	
	descripcion= models.CharField(null=True,blank=True,max_length=300)
	titulo= models.CharField(null=True,blank=True,max_length=10)	
	img=models.FileField(upload_to='imgRespSocial/')
	

	def __unicode__(self):
		return self.titulo

class DetalleProducto(models.Model):
	memoria = models.CharField(max_length=100)
	sisope= models.CharField(null=True,blank=True,max_length=300)	
	fecha_max=models.DateField(auto_now=False)
	def __unicode__(self):
		return self.memoria

TIPO = (
	('Laptop','Laptop'),
	('Notebook','Notebook')
)

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion= models.CharField(null=True,blank=True,max_length=300)
	marca= models.CharField(null=True,blank=True,max_length=100)		
	precio=models.IntegerField(max_length=3,default=0)
	detalle=models.ForeignKey(DetalleProducto)
	tipo = models.CharField(null=True,blank=True,choices=TIPO,max_length=30)
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Producto, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	nombre = models.CharField(max_length=100)
	fecha= models.DateField(auto_now=False)
	img=models.FileField(upload_to='imgEvento/')
	descripcion= models.CharField(null=True,blank=True,max_length=300)
	slug = models.SlugField(max_length=100)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Evento, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre