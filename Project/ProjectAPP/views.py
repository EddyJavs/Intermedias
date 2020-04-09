from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from ProjectAPP.forms import *
from ProjectAPP.models import *
from datetime import datetime,timedelta
from django.contrib import messages
from django.core.mail import EmailMessage

from django.shortcuts import render
import json
import time 
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime,timedelta
from django.db.models import Count, Case, When
from itertools import chain
from operator import attrgetter
from django.core.mail import EmailMessage
from django.db import connection
# Create your views here.
def InsertarUsuario(request):
	return render(request,'Home.html',{})

def Login(request):
	bandera="3"
	request.session['correo']=None
	if request.method=='POST':
		form=Formulario_Login(request.POST or None)
		if form.is_valid():#si elformulario es valido
			datos=form.cleaned_data
			Correo=datos.get("Correo")
			Contrasena=datos.get("Contrasena")
			print (Correo)
			print (Contrasena)
			obj2=usuario.objects.all()
			for usr in obj2:
				print(usr.nombre)
			obj=Usuario.objects.filter(nombre=Correo,password=Contrasena)
			if obj :
				print("correo y contra correcto")
				#verifico si esta dado de alta:
				if obj[0].estado==1:
					for usuario in obj:
					
						request.session["correo"]=usuario.correo
					bandera="1"
					#mando a  la pagina de inicio
					return HttpResponseRedirect('/Inicio/')
				else:
					print("El usuario esta dado de baja")
			else:
				print("correo o contra incorrecto")
				#mensaje error
				bandera="0"
				#return HttpResponse('Incorrecto')
			
			#db_Registro=Estudiante(carnet=carnet_Est,nombre=nombre_Est,carrera=carrera_Est)
			#db_Registro.save()
			#newEstudent=form.save()
			#return HttpResponseRedirect('/Gracias/')#redirigo a esta pagina
	else:
		form=Formulario_Login()#
	context={'form':form,'bandera':bandera}
	return render(request,'Login.html',context)


def Registro_Usuario(request):
	if request.method=='POST':
		form=Formulario_Registro(request.POST or NONE)
		if form.is_valid():#si elformulario es valido
			datos=form.cleaned_data
			Nombre=datos.get("Nombre")
			Apellido=datos.get("Apellido")
			Contrasena=datos.get('Contrasena')
			Correo=datos.get("Correo")
			Telefono=datos.get("Telefono")
			Genero=datos.get("Genero")
			Fecha_nacimiento=datos.get("Fecha_nacimiento")
			formatedDate=Fecha_nacimiento.strftime("%Y-%m-%d")
			Direccion=datos.get("Direccion")
			Pais=datos.get("Pais")
			#Fecha_Registro=time.strftime("")
			Fecha_Registro=datetime.now()
			formatedDateR=Fecha_Registro.strftime("%Y-%m-%d")
			Tipo=1
			Rol=3
			Estado=2
			
			db_Registro=Usuario(nombre=Nombre,apellido=Apellido,clave=Contrasena,correo=Correo,telefono=Telefono,genero=Genero,
				fecha_nacimiento=formatedDate,fecha_registro=formatedDateR,direccion=Direccion,pais=Pais,
				tipo=Tipo,rol=Rol,estado=Estado
				)
			db_Registro.save()
			request.session['correo']=Correo
			txt="para completar el registro haz click en el link para autenticar tu cuenta, \n \n 0.0.0.0:8000/Auth/"+Correo+ "\n\n Si no haz sido tu quien se registro en soccer stats Ignora el correo"
			email = EmailMessage('Completa registro ', txt, to=[Correo])
			email.send()
			return HttpResponseRedirect('/Gracias/')#redirigo a esta pagina
	else:
		form=Formulario_Registro()#
	return render(request,'Registro.html',{'form':form,})


def Gracias(request):
	html='<html><body>Verifique su correo para finalizar el registro</body><html>'
	return HttpResponse(html)
