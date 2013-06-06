from principal.models import *
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


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



#Admin Usuario
class UserCreationForm(forms.ModelForm):
	"""A form for creating new users. Includes all the required
	fields, plus a repeated password."""
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = MyUser
		fields = ('username', 'email')

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = MyUser

	def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
		return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
	form = UserChangeForm
	add_form = UserCreationForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('username', 'email')
	list_filter = ('is_admin',)
	fieldsets = (
			(None, {'fields': ('username', 'password')}),
			('Personal info', {'fields': ('email','dni','direccion','distrito','provincia','departamento','telefono','slug',)}),
			('Permissions', {'fields': ('is_admin',)}),
			('Groups', {'fields': ('tipo_usuario',)}),
			('Important dates', {'fields': ('last_login',)}),
		)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'tipo_usuario', 'password1', 'password2')}#campos necesarios para crear un usuario
		),
	)
	search_fields = ('username',)
	ordering = ('username',)
	filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's builtin permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)