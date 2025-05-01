from django.db import models
from django.contrib.auth.models import User


#se crean las tablas que estarán contenidas en la base de datos
class TUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nombre=models.CharField(max_length=100)
    #primer_apellido=models.CharField(max_length=100)
    segundo_apellido=models.CharField(max_length=100)
    celular=models.CharField(max_length=30)
    tel_fijo=models.CharField(max_length=30)
    ciudad=models.CharField(max_length=255)
    direccion=models.CharField(max_length=100)
    sexo=models.Choices()
    genero=models.CharField()
    estado_civil=models.CharField()
    fecha_nacimiento=models.DateField()
    grupo_sanguineo=models.CharField(max_length=4)
    lugar_tipo_procedencia=models.Choices()
    matricula_profesional=models.CharField(max_length=255)
    

    numero_documento=models.CharField(max_length=50)
    
    #correo=models.CharField(max_length=255)
    
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
        
class Paises(models.Model):
    nombre_pais=models.CharField(max_length=100)

class Departamentos(models.Model):
    nombre_departamento=models.CharField(max_length=100)

class Ciudades(models.Model):
    nombre_ciudad=models.CharField(max_length=100)
    
class TipoDocumentos(models.Model):
    tipo_documento=models.CharField(max_length=100)

class TipoRoles(models.Model):
    tipo_profesional=models.CharField(max_length=100)

class Roles(models.Model):
    tipo_rol=models.CharField(max_length=100)

class Logins(models.Model):
    tipo_r=models.CharField(max_length=100)
   
class DatosSocioeconomicos(models.Model):
    actividad_desempeñada=models.CharField(max_length=100)

class Habitos(models.Model):
    nombre_actividad=models.CharField(max_length=100)

class Espiritualidades(models.Model):
    nombre_religion=models.CharField(max_length=100)

class SeguridadesSociales(models.Model):
    tipo_regimen=models.CharField(max_length=100)

class GradosEscolaridad(models.Model):
    lectura=models.CharField(max_length=100)

class HistoriaGerontologica(models.Model):
    actividad_desempeñada=models.CharField(max_length=100)

class RevisionSistemas(models.Model):
    observaciones_sistemas=models.CharField(max_length=100)

class RevisionSistemas(models.Model):
    observaciones_sistemas=models.CharField(max_length=100)  

class AlteracionSentidos(models.Model):
    cataratas=models.CharField(max_length=100)    

class SistemasRespiratorios(models.Model):
    epoc=models.CharField(max_length=100) 

class SistemasUrinarios(models.Model):
    anuria=models.CharField(max_length=100)

class SistemasEndocrinos(models.Model):
    diabetes_mellitus=models.CharField(max_length=100) 

class SistemasCardiovasculares(models.Model):
    infarto_miocardio=models.CharField(max_length=100) 

class SistemasOseosMusculares(models.Model):
    artritis=models.CharField(max_length=100) 

class SistemasIntergumentarios(models.Model):
    prurito=models.CharField(max_length=100) 

class SistemasDigestivos(models.Model):
    gastritis=models.CharField(max_length=100) 

class SistemasNerviosos(models.Model):
    demencia_senil=models.CharField(max_length=100) 

class Tumores(models.Model):
    tejido_mamario=models.CharField(max_length=100) 

class SituacionesGerontologicas(models.Model):
    fk=models.CharField(max_length=100) 

class Evaluaciones_bucales(models.Model):
    criterio=models.CharField(max_length=100) 

class SindromesProblemas(models.Model):
    vertigo=models.CharField(max_length=100) 


class AspectosFuncionales(models.Model):
    fk=models.CharField(max_length=100) 

class IndiceKATZ(models.Model):
    Alimentacion=models.CharField(max_length=100) 

class AyudasOrtopedicas(models.Model):
    caminador=models.CharField(max_length=100) 

class AspectosPsicogerontologicos(models.Model):
    fk=models.CharField(max_length=100) 

class EnfermedadesMentales(models.Model):
    Psicosis=models.CharField(max_length=100) 

class DepresionesYasavage(models.Model):
    vida_satisfactoria=models.CharField(max_length=100) 

class Valoraciones_mentales(models.Model):
    pregunta_fecha_actual=models.CharField(max_length=100) 

class AspectosFisicos(models.Model):
    estado_fisico=models.CharField(max_length=100) 

class Medicamentos(models.Model):
    nombre_medicamento=models.CharField(max_length=100) 

class AntecedentesToxicos(models.Model):
    Alcohol=models.CharField(max_length=100) 

class Adversidades(models.Model):
    alergia_medicamento=models.CharField(max_length=100) 

class RelacionFamilias(models.Model):
    tipo_relacion=models.CharField(max_length=100) 

class TipoProteccionExequiales(models.Model):
    proteccion=models.CharField(max_length=100) 

class EvolucionesMensuales(models.Model):
    seguimiento=models.CharField(max_length=100) 

class ValoracionesGerontologicas(models.Model):
    aspectos_sociales=models.CharField(max_length=100) 






