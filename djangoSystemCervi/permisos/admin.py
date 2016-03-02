from django.contrib import admin
from .models import Permission

@admin.register(Permission)
# Register your models here.
class AdminPermissions(admin.ModelAdmin):
	list_display = ('asks', 'reason', 'reference')
