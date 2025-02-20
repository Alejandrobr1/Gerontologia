from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TUsuario(models.Model):
    nombre=models.CharField(max_length=100)
    primer_apellido=models.CharField(max_length=100)
    segundo_apellido=models.CharField(max_length=100)
    documento=models.CharField(max_length=50)
    celular=models.CharField(max_length=30)
    correo=models.CharField(max_length=255)
    ciudad=models.CharField(max_length=255)
    direccion=models.CharField(max_length=100)
    rol=models.BooleanField(blank=False)

    def __str__(self):
        return self.nombre +' '+ self.primer_apellido +' '+ self.segundo_apellido

class TLogin(models.Model):
    fk_iduser=models.ForeignKey(TUsuario, on_delete=models.CASCADE)
    contrasena=models.CharField(max_length=100)
    def __str__(self):
        return self.fk_iduser.correo
        
