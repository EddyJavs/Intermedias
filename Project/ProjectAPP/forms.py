from django import forms
from ProjectAPP import views
from ProjectAPP.models import *
from datetime import date
TIME_FORMAT='%Y-%m-%d'
#from SoccerStats import settings
class Formulario_Login(forms.Form):
	Correo= forms.EmailField()
	Contrasena = forms.CharField()
	
Roles_list=(('Vendedor','Vendedor'),('Bodeguero','Bodeguero'),('Repartidor','Repartidor'))
class Formulario_Registro(forms.Form):
	DPI = forms.CharField()
	Nombre = forms.CharField()
	Fecha_nacimiento = forms.DateField(input_formats=[TIME_FORMAT])
	Correo = forms.EmailField()
	Contrasena = forms.CharField()
	Roles = forms.CharField()
	Permisos = forms.ChoiceField(choices=Roles_list)
	



