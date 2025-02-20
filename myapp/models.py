from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tlogin(models.Model):
    idlogin=models.BigIntegerField
    fk_iduser=models.ForeignKey(User)
    contrasena=models.CharField(max_length=100)




    """nombre=models.CharField(max_length=100),
    primer_apellido=models.CharField(max_length=100),
    segundo_apellido=models.CharField(max_length=100),
    documento=models.CharField(max_length=50),
    celular=models.CharField(max_length=30),
    correo=models.CharField(max_length=255),
    ciudad=models.CharField(max_length=255),
    direccion=models.CharField(max_length=100),
    rol=models.BooleanField(blank=False)"""



