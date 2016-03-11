from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cliente

def adminClient(request):
	cliente = Cliente.objects.order_by('id')
	template = loader.get_template('index.html')
	title = 'Administracion de Clientes'
	context = {
		'cliente': cliente,
		'title': title
	}
	return HttpResponse(template.render(context, request))


def saludo(request):
	template = loader.get_template('saludo.html')
	big_title = 'Encabezado de la pagina'
	title = 'SAludo nuevo'
	context = {
	'big_title': big_title,
	'title': title

	}

	return HttpResponse(template.render(context, request))
