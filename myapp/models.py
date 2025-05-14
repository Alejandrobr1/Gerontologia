from django.db import models
from django.contrib.auth.models import User
#se definen las tablas que estarán contenidas en la base de datos

class Paises(models.Model):
    nombre_pais=models.CharField(max_length=255)

class Departamentos(models.Model):
    nombre_departamento=models.CharField(max_length=255)
    fk_pais=models.ForeignKey(Paises, on_delete=models.PROTECT)

class Ciudades(models.Model):
    nombre_ciudad=models.CharField(max_length=100)
    fk_departamento=models.ForeignKey(Departamentos, on_delete=models.PROTECT)

TIPO_DOCUMENTO={
        "RC" : "Registro Civil",
        "TI" : "Tarjeta de Identidad",
        "TE" : "Tarjeta de Extranjeria",
        "CE" : "Cedula de Extranjeria",
        "NIT" : "Número de identificación Tributaria",
        "PP" : "Pasaporte",
        "PEP" : "Permiso Especial de Permanencia",
        "DIE" : "Documento de identificación extranjero",
        "NUIP" : "NUIP",
        "FOREIGN_NIT" : "NIT de otro pais",
    } 
class TipoDocumentos(models.Model):
    tipo_documento=models.CharField(max_length=11,choices=TIPO_DOCUMENTO)
    
class DatosSocioeconomicos(models.Model):
    actividad_desempeñada=models.CharField(max_length=255)
    actividad_actual=models.CharField(max_length=255)
    tipo_ingreso=models.CharField(max_length=255)
    valor_mensual_promedio=models.FloatField()
    clasificacion_ingreso=models.CharField(max_length=255)

class Habitos(models.Model):
    persona_activa=models.BooleanField(default=False)
    nombre_actividad=models.CharField(max_length=255, blank=True, null=True)
    actividad_fisica=models.CharField(max_length=255, blank=True, null=True)

class Espiritualidades(models.Model):
    pertenece_grupo_religioso=models.BooleanField(default=True)
    nombre_religion=models.CharField(max_length=255, blank=True, null=True)
    actividad_espiritual=models.CharField(max_length=255, blank=True, null=True)


class SeguridadesSociales(models.Model):
    TIPO_REGIMEN={
        "C" : "Contributivo",
        "S" : "Subsidiado",
        "E" : "Especial",
        "N" : "Ninguno"
    }
    tipo_regimen=models.CharField(max_length=1,
                          choices=TIPO_REGIMEN)
    nombre_eps=models.CharField(max_length=255,blank=True, null=True)
    nombre_ips=models.CharField(max_length=255, blank=True, null=True)

class GradosEscolaridad(models.Model):
    lee=models.BooleanField(default=True)
    escribe=models.BooleanField(default=True)
    tiene_primaria=models.BooleanField(default=True)
    primaria_finalizada=models.BooleanField(default=True)
    tiene_secundaria=models.BooleanField(default=True)
    secundaria_finalizada=models.BooleanField(default=True)
    tiene_tecnica=models.BooleanField(default=True)
    nombre_tecnica=models.CharField(max_length=100)
    tiene_tecnologia=models.BooleanField(default=True)
    nombre_tecnologia=models.CharField(max_length=100)
    tiene_pregrado=models.BooleanField(default=True)
    nombre_pregrado=models.CharField(max_length=100)
    tiene_posgrado=models.BooleanField(default=True)
    nombre_posgrado=models.CharField(max_length=100)
    otro_estudio=models.BooleanField(default=True)
    nombre_otro_estudio=models.CharField(max_length=100)
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    segundo_apellido=models.CharField(max_length=100, blank=True)
    celular=models.CharField(max_length=30, blank=True)
    tel_fijo=models.CharField(max_length=30, default="N/A")
    direccion=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    grupo_sanguineo=models.CharField(max_length=3) 
    genero=models.CharField(max_length=50)
    matricula_profesional=models.CharField(max_length=255, default="N/A")
    numero_documento=models.CharField(max_length=50)
    fk_ciudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    fk_tipo_documento=models.ForeignKey(TipoDocumentos, on_delete=models.CASCADE)
    fk_datos_socioeconomicos=models.OneToOneField(DatosSocioeconomicos, on_delete=models.CASCADE) #verificar onetoone o foreignkey
    fk_habitos=models.OneToOneField(Habitos,on_delete=models.CASCADE)
    fk_espiritualidades=models.OneToOneField(Espiritualidades,on_delete=models.CASCADE)
    fk_seguridades_sociales=models.OneToOneField(SeguridadesSociales,on_delete=models.CASCADE)
    SEXO={
        "M" : "Masculino",
        "F" : "Femenino"
    }
    sexo=models.CharField(max_length=1,
                          choices=SEXO)

    ESTADO_CIVIL={
        "S": "Soltero",
        "C": "Casado",
        "V": "Viudo",
        "D": "Divorciado",
        "UL": "Union Libre"
    }
    estado_civil=models.CharField(max_length=11,
                                  choices=ESTADO_CIVIL) 

    TIPO_PROCEDENCIA={
        "U" : "Urbano",
        "R" : "Rural"
    }
    lugar_tipo_procedencia=models.CharField(max_length=1,
                                            choices=TIPO_PROCEDENCIA)

    
    
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


"""
class TipoRoles(models.Model):
    tipo_profesional=models.CharField(max_length=100)

class Roles(models.Model):
    tipo_rol=models.CharField(max_length=100)

class Logins(models.Model):
    tipo_r=models.CharField(max_length=100)
"""   

class TipoFamilias(models.Model):
    familia_nuclear=models.BooleanField(default=False)
    familia_extensa=models.BooleanField(default=False)
    familia_ampliada=models.BooleanField(default=False)
    familia_multiespecial=models.BooleanField(default=False)
    familia_compuesta=models.BooleanField(default=False)
    familia_monoparental_simple=models.BooleanField(default=False)
    familia_monoparental_compuesta=models.BooleanField(default=False)
    familia_homoparental=models.BooleanField(default=False)
    familia_unipersonal=models.BooleanField(default=False)
    familia_pareja_sin_hijos=models.BooleanField(default=False)
    familia_mixta=models.BooleanField(default=False)
    unidad_domestica=models.BooleanField(default=False)

class RelacionFamilias(models.Model):
    relacion_mala=models.TextField(blank=True)
    maltrato=models.BooleanField(default=False)
    tipo_maltrato=models.CharField(max_length=255, blank=True, null=True)
    TIPO_RELACION={
        "B" : "Buena",
        "M" : "Mala",
        "R" : "Regular"
    }
    tipo_relacion=models.CharField(max_length=1, 
                                   choices=TIPO_RELACION) 

class TipoProteccionesExequiales(models.Model):
    proteccion=models.BooleanField(default=False)
    nombre_entidad=models.CharField(max_length=255, blank=True)

class ValoracionesGerontologicas(models.Model):
    aspecto_sociales=models.CharField(max_length=100) 
    aspecto_fisicos=models.CharField(max_length=100) 
    aspectos_funcional=models.CharField(max_length=100) 
    aspectos_psicogerontologico=models.CharField(max_length=100) 
class AlteracionSentidos(models.Model):
    cataratas=models.BooleanField(default=False)    
    ceguera=models.BooleanField(default=False)    
    glaucoma=models.BooleanField(default=False)    
    presbiacusia=models.BooleanField(default=False)    
    otra_alteracion_sentidos=models.CharField(max_length=255, blank=True, null=True)    

class SistemasRespiratorios(models.Model):
    epoc=models.BooleanField(default=False) 
    bronquitis=models.BooleanField(default=False) 
    asma=models.BooleanField(default=False) 
    neumonia=models.BooleanField(default=False) 
    otra_alteracion_respiratoria=models.CharField(max_length=255, blank=True, null=True)    

class SistemasUrinarios(models.Model):
    anuria=models.BooleanField(default=False) 
    cistitis=models.BooleanField(default=False) 
    prostatitis=models.BooleanField(default=False) 
    prolapso_genital=models.BooleanField(default=False) 
    incontinencia=models.BooleanField(default=False) 
    otra_alteracion_urinaria=models.CharField(max_length=255, blank=True, null=True)     

class SistemasEndocrinos(models.Model):
    diabetes_mellitus=models.BooleanField(default=False) 
    hipertiroidismo=models.BooleanField(default=False) 
    hipotiroidismo=models.BooleanField(default=False) 
    bocio=models.BooleanField(default=False) 
    incontinencia=models.BooleanField(default=False) 
    otra_alteracion_endocrina=models.CharField(max_length=255, blank=True, null=True)    

class SistemasCardiovasculares(models.Model):
    infarto_miocardio=models.BooleanField(default=False) 
    HTA=models.BooleanField(default=False) 
    insuficiencia_cardiaca=models.BooleanField(default=False) 
    arteriosclerosis=models.BooleanField(default=False) 
    otra_alteracion_cardiovascular=models.CharField(max_length=255, blank=True, null=True)    

class SistemasOseosMusculares(models.Model):
    artritis=models.BooleanField(default=False) 
    osteoporosis=models.BooleanField(default=False) 
    osteartritis=models.BooleanField(default=False) 
    lumbago=models.BooleanField(default=False) 
    otra_alteracion_osea=models.CharField(max_length=255, blank=True, null=True)    

class SistemasIntergumentarios(models.Model):
    prurito=models.BooleanField(default=False) 
    urticaria=models.BooleanField(default=False) 
    verruga=models.BooleanField(default=False) 
    quemadura=models.BooleanField(default=False)  
    otra_alteracion_intergumentaria=models.CharField(max_length=255, blank=True, null=True)    

class SistemasDigestivos(models.Model):
    gastritis=models.BooleanField(default=False) 
    diarrea=models.BooleanField(default=False) 
    estrenhimiento=models.BooleanField(default=False) 
    ulcera_duodenal=models.BooleanField(default=False) 
    otra_alteracion_digestiva=models.CharField(max_length=255, blank=True, null=True)    
class Tumores(models.Model):
    tejido_mamario=models.BooleanField(default=False) 
    sistema_digestivo=models.BooleanField(default=False) 
    sistema_urinario=models.BooleanField(default=False) 
    otra_tumor=models.CharField(max_length=255, blank=True, null=True)    
class SistemasNerviosos(models.Model):
    demencia_senil=models.BooleanField(default=False) 
    alzheimer=models.BooleanField(default=False) 
    parkinson=models.BooleanField(default=False) 
    esquizofrenia=models.BooleanField(default=False) 
    eilepsia=models.BooleanField(default=False) 
    otra_alteracion_nerviosa=models.CharField(max_length=255, blank=True, null=True)    

class RevisionSistemas(models.Model):
    observaciones_sistemas=models.TextField()
    fk_alteraciones_sentidos=models.OneToOneField(AlteracionSentidos, on_delete=models.CASCADE)  
    fk_sistemas_respiratorios=models.OneToOneField(SistemasRespiratorios, on_delete=models.CASCADE)  
    fk_sistemas_urinarios=models.OneToOneField(SistemasUrinarios, on_delete=models.CASCADE)  
    fk_sistemas_endocrinos=models.OneToOneField(SistemasEndocrinos, on_delete=models.CASCADE)  
    fk_sistemas_cardiovasculares=models.OneToOneField(SistemasCardiovasculares, on_delete=models.CASCADE)  
    fk_sistemas_oseo_musculares=models.OneToOneField(SistemasOseosMusculares, on_delete=models.CASCADE)  
    fk_sistemas_intergumentarios=models.OneToOneField(SistemasIntergumentarios, on_delete=models.CASCADE)  
    fk_sistemas_digestivos=models.OneToOneField(SistemasDigestivos, on_delete=models.CASCADE)  
    fk_tumores=models.OneToOneField(Tumores, on_delete=models.CASCADE)  
    fk_sistemas_nerviosos=models.OneToOneField(SistemasNerviosos, on_delete=models.CASCADE)  


class Evaluaciones_bucales(models.Model):
    valoracion=models.CharField(max_length=255, blank=True , null=True)
    observacion=models.TextField(blank=True)
    CRITERIO={
        "PC" : "Piezas Completas",
        "PI" : "Piezas incompletas",
        "PRO" : "Potesis"
    }
    criterio=models.CharField(max_length=3,
                            choices=CRITERIO)  

class SindromesProblemas(models.Model):
    vertigo=models.BooleanField(default=False) 
    delirio=models.BooleanField(default=False) 
    caidas=models.BooleanField(default=False) 
    numero_caidas_fractura=models.SmallIntegerField() 
    sincope=models.BooleanField(default=False) 
    dolor_cronio=models.BooleanField(default=False) 
    deprivacion_auditiva=models.BooleanField(default=False) 
    deprivacion_visual=models.BooleanField(default=False) 
    insomnio=models.BooleanField(default=False) 
    incontinencia_urinaria=models.BooleanField(default=False) 
    prostatismo=models.BooleanField(default=False) 
    estrenhimiento=models.BooleanField(default=False) 
    ulcera_presion=models.BooleanField(default=False) 
    inmovilizacion=models.BooleanField(default=False) 
    cirugia=models.BooleanField(default=False) 
    numero_cirugias=models.SmallIntegerField() 
    observacion_sindromes_problemas=models.TextField(blank=True, null=True)

class SituacionesGerontologicas(models.Model):
    fk_evaluaciones_bucales=models.OneToOneField(Evaluaciones_bucales, on_delete=models.CASCADE) 
    fk_sindromes_problemas=models.OneToOneField(SindromesProblemas, on_delete=models.CASCADE) 


class IndiceKATZ(models.Model):
    alimentacion=models.BooleanField(default=False) 
    baño=models.BooleanField(default=False) 
    continencia=models.BooleanField(default=False) 
    movilidad=models.BooleanField(default=False)  
    uso_WC=models.BooleanField(default=False) 
    vetido=models.BooleanField(default=False) 
    total_puntuacion=models.SmallIntegerField()
    resultado=models.CharField(max_length=255)
    observacion_indice_KATZ=models.TextField(blank=True, null=True)

class AyudasOrtopedicas(models.Model):
    caminador=models.BooleanField(default=False) 
    muletas=models.BooleanField(default=False) 
    silla_ruedas=models.BooleanField(default=False) 
    baston=models.BooleanField(default=False) 
    gafas=models.BooleanField(default=False) 
    audifonos=models.BooleanField(default=False) 
    protesis=models.BooleanField(default=False)
    otra_ayuda_ortopedica=models.CharField(max_length=255)
    observacion_ayuda_ortopedica=models.TextField(blank=True, null=True)
 
class AspectosFuncionales(models.Model):
    fk_ayudas_ortopedicas=models.OneToOneField(AyudasOrtopedicas, on_delete=models.CASCADE) 
    fk_indice_KATZ=models.OneToOneField(IndiceKATZ, on_delete=models.CASCADE) 
    observacion_aspectos_funcionales=models.TextField(blank=True, null=True)

class EnfermedadesMentales(models.Model):
    psicosis=models.BooleanField(default=False) 
    transtorno_ansiedad=models.BooleanField(default=False) 
    problema_intergeneracional=models.BooleanField(default=False) 
    duelo_patologico=models.BooleanField(default=False) 
    transtorno_afectivo_bipolar=models.BooleanField(default=False)
    depresion=models.BooleanField(default=False)
    IDEAS_SUICIDAS={
        "SI" : "Si",
        "NO" : "No",
        "AV" : "A veces"
    }
    ideas_suicidas=models.CharField(max_length=2,
                                    choices=IDEAS_SUICIDAS)
    observacion_suicidio=models.TextField(blank=True, null=True)
 

class DepresionesYasavage(models.Model):
    vida_satisfactoria=models.BooleanField(default=False) 
    renuncia=models.BooleanField(default=False) 
    vacio=models.BooleanField(default=False) 
    aburrido=models.BooleanField(default=False) 
    optimista=models.BooleanField(default=False) 
    temor=models.BooleanField(default=False) 
    feliz=models.BooleanField(default=False) 
    desamparado=models.BooleanField(default=False) 
    quedarse_casa=models.BooleanField(default=False) 
    fallo_memoria=models.BooleanField(default=False) 
    vivir=models.BooleanField(default=False) 
    nuevo_proyecto=models.BooleanField(default=False) 
    energia=models.BooleanField(default=False) 
    angustia=models.BooleanField(default=False) 
    economia=models.BooleanField(default=False) 
    total_puntuacion_depresion=models.SmallIntegerField()  
    resultado=models.CharField(max_length=20)  
class ValoracionesMentales(models.Model):
    fecha_actual_pregunta=models.BooleanField(default=False)  
    dia_semana_pregunta=models.BooleanField(default=False) 
    lugar_pregunta=models.BooleanField(default=False) 
    lugar_nacimiento_pregunta=models.BooleanField(default=False) 
    presidente_pregunta=models.BooleanField(default=False) 
    primer_apellido_madre_pregunta=models.BooleanField(default=False) 
    resta_pregunta=models.BooleanField(default=False) 
    total_puntuacion_valoracion_mental=models.SmallIntegerField()  
    resultado=models.CharField(max_length=20)  

class AspectosPsicogerontologicos(models.Model):
    fk_enfermedades_mentales=models.OneToOneField(EnfermedadesMentales, on_delete=models.CASCADE) 
    fk_depresiones_yasavage=models.OneToOneField(DepresionesYasavage, on_delete=models.CASCADE) 
    fk_valoraciones_mentales=models.OneToOneField(ValoracionesMentales, on_delete=models.CASCADE) 
    

class Medicamentos(models.Model):
    nombre_medicamento=models.CharField(max_length=255) 
    dosis=models.CharField(max_length=255)
    observacion_medicamento=models.CharField(max_length=255, blank=True, null=True)
    alergia=models.BooleanField(default=False) 
    nombre_alergia=models.CharField(max_length=255)
class AntecedentesToxicos(models.Model):
    alcohol=models.BooleanField(default=False) 
    frecuencia_alcohol=models.CharField(max_length=255)  
    cigarrillo=models.BooleanField(default=False) 
    frecuencia_cigarrillo=models.CharField(max_length=255) 
    cafe=models.BooleanField(default=False) 
    frecuencia_cafe=models.CharField(max_length=255) 
    sustancia_psicoactiva=models.BooleanField(default=False) 
    frecuencia_sustancia=models.CharField(max_length=255) 
class Adversidades(models.Model):
    alergia_medicamento=models.BooleanField(default=False) 
    nombre_alergia_medicamento=models.CharField(max_length=255)  
    autoprescripcion=models.BooleanField(default=False) 
    nombre_autoprescripcion=models.CharField(max_length=255) 
    alergia_alimento=models.BooleanField(default=False) 
    nombre_alergia_alimento=models.CharField(max_length=255) 
class AspectosFisicos(models.Model):
    ESTADO_FISICO={
        "B" : "Bueno",
        "M" : "Malo",
        "R" : "Regular"
    }
    estado_fisico=models.CharField(max_length=2,
                                    choices=ESTADO_FISICO)
    condicion_malo=models.TextField(blank=True, null=True)
    fk_medicamentos=models.ForeignKey(Medicamentos, on_delete=models.CASCADE) 
    fk_antecedentes_toxicos=models.OneToOneField(AntecedentesToxicos, on_delete=models.CASCADE) 
    fk_adversidades=models.OneToOneField(Adversidades, on_delete=models.CASCADE) 
    
class HistoriasGerontologicas(models.Model):
    numero_historia=models.IntegerField(primary_key=id)
    fecha_consulta=models.DateField()
    fecha_elaboracion=models.DateField()
    fecha_ingreso=models.DateField()
    fecha_egreso=models.DateField()
    actividad_desempeñada=models.CharField(max_length=100)
    observaciones_historia_gerontologica=models.TextField(blank=True)
    fk_usuarios=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_tipo_familias=models.OneToOneField(TipoFamilias, on_delete=models.CASCADE)
    fk_relacion_familias=models.OneToOneField(RelacionFamilias, on_delete=models.CASCADE)
    fk_tipo_protecciones_exequiales=models.OneToOneField(TipoProteccionesExequiales, on_delete=models.CASCADE)
    fk_valoraciones_gerontologicas=models.OneToOneField(ValoracionesGerontologicas, on_delete=models.CASCADE)
    fk_revision_sistemas=models.OneToOneField(RevisionSistemas, on_delete=models.CASCADE)
    fk_situaciones_gerontologicas=models.OneToOneField(SituacionesGerontologicas, on_delete=models.CASCADE)
    fk_aspectos_funcionales=models.OneToOneField(AspectosFuncionales, on_delete=models.CASCADE)
    fk_aspectos_psicogerontologicos=models.OneToOneField(AspectosPsicogerontologicos, on_delete=models.CASCADE)
    fk_aspectos_fisicos=models.OneToOneField(AspectosFisicos, on_delete=models.CASCADE)   
    MOTIVO={
        "I" : "Ingreso",
        "E" : "Egreso"
    }
    motivo=models.CharField(max_length=1,
                            choices=MOTIVO)  
class EvolucionesMensuales(models.Model):
    seguimiento=models.TextField(blank=True) 
    fecha_evolucion=models.DateField()
    fk_historias_gerontologicas=models.ForeignKey(HistoriasGerontologicas, on_delete=models.CASCADE)

