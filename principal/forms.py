from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

class ContactoForm(ModelForm):
	nombre= forms.RegexField(label="Nombres:", max_length=30, regex=r'^[a-zA-Z ]+$', help_text = "Indica tus nombres", error_message = "Solo letras")
	e_mail= forms.EmailField(label="Email", help_text = "Indica tu email",widget=forms.TextInput(attrs={'class': 'required', 'maxlength':75}) )
	class Meta:
		model = Contactenos

class SuscripcionForm(ModelForm):
	class Meta:
		model=Suscripcion