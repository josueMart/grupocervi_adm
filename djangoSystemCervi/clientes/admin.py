from django.contrib import admin
from .models import Cliente

# Register your models here.

#admin.site.register(Cliente)
@admin.register(Cliente)
#Esta clase permite mostrar mas campos en el admin de la tabla
class AdminCliente(admin.ModelAdmin):
	list_display = ('name','address','contactName','email')
	list_filter = ('name', 'contactName') 