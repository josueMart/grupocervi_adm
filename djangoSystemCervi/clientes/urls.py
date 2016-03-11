from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.adminClient, name='Clientes'),
	url(r'^saludo/', views.saludo, name='Clientes') 
]