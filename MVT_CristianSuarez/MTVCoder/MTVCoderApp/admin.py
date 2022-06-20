from django.contrib import admin

from MTVCoderApp.models import Familiar

# Register your models here.
class FamiliarAdmin(admin.ModelAdmin):
     
    list_display = ('nombre', 'apellido', 'edad', 'fecha_nacimiento')

admin.site.register(Familiar, FamiliarAdmin)