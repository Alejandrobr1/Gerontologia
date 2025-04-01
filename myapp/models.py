from django.db import models
from django.contrib.auth.models import User


#se crean las tablas que estarán contenidas en la base de datos
class TUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nombre=models.CharField(max_length=100)
    #primer_apellido=models.CharField(max_length=100)
    segundo_apellido=models.CharField(max_length=100)
    documento=models.CharField(max_length=50)
    celular=models.CharField(max_length=30)
    #correo=models.CharField(max_length=255)
    ciudad=models.CharField(max_length=255)
    direccion=models.CharField(max_length=100)
    #profesional=models.CharField(max_length=255)
    #fk_iduser=models.ForeignKey(User, on_delete=models.CASCADE)
    


""" def __str__(self): #Este metodo se encargara de mostrar el nombre del usuario desde el administrador de Django
        return self.segundo_apellido
        #return self.nombre +' '+ self.primer_apellido +' '+ self.segundo_apellido """

"""class TLogin(models.Model):
    fk_iduser=models.ForeignKey(TUsuario, on_delete=models.CASCADE)
    contrasenaLogin=models.CharField(max_length=100)
    def __str__(self):#Este metodo se encargara de mostrar el correo del usuario desde el administrador de Django
        return self.fk_iduser.correo"""
        
