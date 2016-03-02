from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cliente

def adminClient(request):
	cliente = Cliente.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'cliente': cliente
	}
	return HttpResponse(template.render(context, request))
# Create your views here.
