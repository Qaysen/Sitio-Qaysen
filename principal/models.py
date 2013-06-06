from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,BaseUserManager
from django.template import defaultfilters
from django.db.models import signals

#Usuarios Admin
class MyUserManager(BaseUserManager):
	def create_user(self, username, email , password=None):
		if not email:
			raise ValueError('The given email must be set')
		user = self.model( username=username, 
						email = MyUserManager.normalize_email(email))

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,username, email ,password):
		user = self.create_user(username, password=password, email=email)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	usuarios = (
		('Administrador','Administrador'),
		('Equipo','Equipo'),
		('Cliente','Cliente'),
	)
	username = models.CharField(max_length=200 , unique=True)
	email = models.EmailField(db_index=True)
	tipo_usuario=models.CharField(choices=usuarios,max_length=12)
	dni = models.CharField(max_length=8,null=True,blank=True)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	distrito =models.CharField(max_length=20,null=True,blank=True)
	provincia=models.CharField(max_length=20,null=True,blank=True)
	departamento=models.CharField(max_length=20,null=True,blank=True)
	telefono=models.CharField(max_length=7,null=True,blank=True)
	slug = models.SlugField()


	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		return self.email
 
	def get_short_name(self):
		return self.email
 
	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

#Fin Usuarios Admin	

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