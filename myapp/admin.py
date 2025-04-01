from django.contrib import admin
from .models import TUsuario #TLogin, 
# Register your models here.
# Este metodo permite acceder a las tablas de TUsuario y TLogin desde el panel de administración de Django.
admin.site.register(TUsuario) 
#admin.site.register(TLogin) 