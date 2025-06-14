# Generated by Django 5.1.6 on 2025-05-14 22:30

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_espiritualidades_gradosescolaridad_habitos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adversidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alergia_medicamento', models.BooleanField(default=False)),
                ('nombre_alergia_medicamento', models.CharField(max_length=255)),
                ('autoprescripcion', models.BooleanField(default=False)),
                ('nombre_autoprescripcion', models.CharField(max_length=255)),
                ('alergia_alimento', models.BooleanField(default=False)),
                ('nombre_alergia_alimento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AlteracionSentidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cataratas', models.BooleanField(default=False)),
                ('ceguera', models.BooleanField(default=False)),
                ('glaucoma', models.BooleanField(default=False)),
                ('presbiacusia', models.BooleanField(default=False)),
                ('otra_alteracion_sentidos', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AntecedentesToxicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcohol', models.BooleanField(default=False)),
                ('frecuencia_alcohol', models.CharField(max_length=255)),
                ('cigarrillo', models.BooleanField(default=False)),
                ('frecuencia_cigarrillo', models.CharField(max_length=255)),
                ('cafe', models.BooleanField(default=False)),
                ('frecuencia_cafe', models.CharField(max_length=255)),
                ('sustancia_psicoactiva', models.BooleanField(default=False)),
                ('frecuencia_sustancia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AspectosFisicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_fisico', models.CharField(choices=[('B', 'Bueno'), ('M', 'Malo'), ('R', 'Regular')], max_length=2)),
                ('condicion_malo', models.TextField(blank=True, null=True)),
                ('fk_adversidades', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.adversidades')),
                ('fk_antecedentes_toxicos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.antecedentestoxicos')),
            ],
        ),
        migrations.CreateModel(
            name='AspectosFuncionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion_aspectos_funcionales', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AspectosPsicogerontologicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AyudasOrtopedicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caminador', models.BooleanField(default=False)),
                ('muletas', models.BooleanField(default=False)),
                ('silla_ruedas', models.BooleanField(default=False)),
                ('baston', models.BooleanField(default=False)),
                ('gafas', models.BooleanField(default=False)),
                ('audifonos', models.BooleanField(default=False)),
                ('protesis', models.BooleanField(default=False)),
                ('otra_ayuda_ortopedica', models.CharField(max_length=255)),
                ('observacion_ayuda_ortopedica', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepresionesYasavage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vida_satisfactoria', models.BooleanField(default=False)),
                ('renuncia', models.BooleanField(default=False)),
                ('vacio', models.BooleanField(default=False)),
                ('aburrido', models.BooleanField(default=False)),
                ('optimista', models.BooleanField(default=False)),
                ('temor', models.BooleanField(default=False)),
                ('feliz', models.BooleanField(default=False)),
                ('desamparado', models.BooleanField(default=False)),
                ('quedarse_casa', models.BooleanField(default=False)),
                ('fallo_memoria', models.BooleanField(default=False)),
                ('vivir', models.BooleanField(default=False)),
                ('nuevo_proyecto', models.BooleanField(default=False)),
                ('energia', models.BooleanField(default=False)),
                ('angustia', models.BooleanField(default=False)),
                ('economia', models.BooleanField(default=False)),
                ('total_puntuacion_depresion', models.SmallIntegerField()),
                ('resultado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EnfermedadesMentales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psicosis', models.BooleanField(default=False)),
                ('transtorno_ansiedad', models.BooleanField(default=False)),
                ('problema_intergeneracional', models.BooleanField(default=False)),
                ('duelo_patologico', models.BooleanField(default=False)),
                ('transtorno_afectivo_bipolar', models.BooleanField(default=False)),
                ('depresion', models.BooleanField(default=False)),
                ('ideas_suicidas', models.CharField(choices=[('SI', 'Si'), ('NO', 'No'), ('AV', 'A veces')], max_length=2)),
                ('observacion_suicidio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluaciones_bucales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.CharField(blank=True, max_length=255, null=True)),
                ('observacion', models.TextField(blank=True)),
                ('criterio', models.CharField(choices=[('PC', 'Piezas Completas'), ('PI', 'Piezas incompletas'), ('PRO', 'Potesis')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='EvolucionesMensuales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguimiento', models.TextField(blank=True)),
                ('fecha_evolucion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoriasGerontologicas',
            fields=[
                ('numero_historia', models.IntegerField(primary_key=builtins.id, serialize=False)),
                ('fecha_consulta', models.DateField()),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_egreso', models.DateField()),
                ('actividad_desempeñada', models.CharField(max_length=100)),
                ('observaciones_historia_gerontologica', models.TextField(blank=True)),
                ('motivo', models.CharField(choices=[('I', 'Ingreso'), ('E', 'Egreso')], max_length=1)),
                ('fk_aspectos_fisicos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.aspectosfisicos')),
            ],
        ),
        migrations.CreateModel(
            name='IndiceKATZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alimentacion', models.BooleanField(default=False)),
                ('baño', models.BooleanField(default=False)),
                ('continencia', models.BooleanField(default=False)),
                ('movilidad', models.BooleanField(default=False)),
                ('uso_WC', models.BooleanField(default=False)),
                ('vetido', models.BooleanField(default=False)),
                ('total_puntuacion', models.SmallIntegerField()),
                ('resultado', models.CharField(max_length=255)),
                ('observacion_indice_KATZ', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(max_length=255)),
                ('dosis', models.CharField(max_length=255)),
                ('observacion_medicamento', models.CharField(blank=True, max_length=255, null=True)),
                ('alergia', models.BooleanField(default=False)),
                ('nombre_alergia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RelacionFamilias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacion_mala', models.TextField(blank=True)),
                ('maltrato', models.BooleanField(default=False)),
                ('tipo_maltrato', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_relacion', models.CharField(choices=[('B', 'Buena'), ('M', 'Mala'), ('R', 'Regular')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionSistemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones_sistemas', models.TextField()),
                ('fk_alteraciones_sentidos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.alteracionsentidos')),
            ],
        ),
        migrations.CreateModel(
            name='SindromesProblemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vertigo', models.BooleanField(default=False)),
                ('delirio', models.BooleanField(default=False)),
                ('caidas', models.BooleanField(default=False)),
                ('numero_caidas_fractura', models.SmallIntegerField()),
                ('sincope', models.BooleanField(default=False)),
                ('dolor_cronio', models.BooleanField(default=False)),
                ('deprivacion_auditiva', models.BooleanField(default=False)),
                ('deprivacion_visual', models.BooleanField(default=False)),
                ('insomnio', models.BooleanField(default=False)),
                ('incontinencia_urinaria', models.BooleanField(default=False)),
                ('prostatismo', models.BooleanField(default=False)),
                ('estrenhimiento', models.BooleanField(default=False)),
                ('ulcera_presion', models.BooleanField(default=False)),
                ('inmovilizacion', models.BooleanField(default=False)),
                ('cirugia', models.BooleanField(default=False)),
                ('numero_cirugias', models.SmallIntegerField()),
                ('observacion_sindromes_problemas', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasCardiovasculares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infarto_miocardio', models.BooleanField(default=False)),
                ('HTA', models.BooleanField(default=False)),
                ('insuficiencia_cardiaca', models.BooleanField(default=False)),
                ('arteriosclerosis', models.BooleanField(default=False)),
                ('otra_alteracion_cardiovascular', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasDigestivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gastritis', models.BooleanField(default=False)),
                ('diarrea', models.BooleanField(default=False)),
                ('estrenhimiento', models.BooleanField(default=False)),
                ('ulcera_duodenal', models.BooleanField(default=False)),
                ('otra_alteracion_digestiva', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasEndocrinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes_mellitus', models.BooleanField(default=False)),
                ('hipertiroidismo', models.BooleanField(default=False)),
                ('hipotiroidismo', models.BooleanField(default=False)),
                ('bocio', models.BooleanField(default=False)),
                ('incontinencia', models.BooleanField(default=False)),
                ('otra_alteracion_endocrina', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasIntergumentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prurito', models.BooleanField(default=False)),
                ('urticaria', models.BooleanField(default=False)),
                ('verruga', models.BooleanField(default=False)),
                ('quemadura', models.BooleanField(default=False)),
                ('otra_alteracion_intergumentaria', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasNerviosos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demencia_senil', models.BooleanField(default=False)),
                ('alzheimer', models.BooleanField(default=False)),
                ('parkinson', models.BooleanField(default=False)),
                ('esquizofrenia', models.BooleanField(default=False)),
                ('eilepsia', models.BooleanField(default=False)),
                ('otra_alteracion_nerviosa', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasOseosMusculares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artritis', models.BooleanField(default=False)),
                ('osteoporosis', models.BooleanField(default=False)),
                ('osteartritis', models.BooleanField(default=False)),
                ('lumbago', models.BooleanField(default=False)),
                ('otra_alteracion_osea', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasRespiratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoc', models.BooleanField(default=False)),
                ('bronquitis', models.BooleanField(default=False)),
                ('asma', models.BooleanField(default=False)),
                ('neumonia', models.BooleanField(default=False)),
                ('otra_alteracion_respiratoria', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SistemasUrinarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anuria', models.BooleanField(default=False)),
                ('cistitis', models.BooleanField(default=False)),
                ('prostatitis', models.BooleanField(default=False)),
                ('prolapso_genital', models.BooleanField(default=False)),
                ('incontinencia', models.BooleanField(default=False)),
                ('otra_alteracion_urinaria', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SituacionesGerontologicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_evaluaciones_bucales', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.evaluaciones_bucales')),
                ('fk_sindromes_problemas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sindromesproblemas')),
            ],
        ),
        migrations.CreateModel(
            name='TipoFamilias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia_nuclear', models.BooleanField(default=False)),
                ('familia_extensa', models.BooleanField(default=False)),
                ('familia_ampliada', models.BooleanField(default=False)),
                ('familia_multiespecial', models.BooleanField(default=False)),
                ('familia_compuesta', models.BooleanField(default=False)),
                ('familia_monoparental_simple', models.BooleanField(default=False)),
                ('familia_monoparental_compuesta', models.BooleanField(default=False)),
                ('familia_homoparental', models.BooleanField(default=False)),
                ('familia_unipersonal', models.BooleanField(default=False)),
                ('familia_pareja_sin_hijos', models.BooleanField(default=False)),
                ('familia_mixta', models.BooleanField(default=False)),
                ('unidad_domestica', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProteccionesExequiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proteccion', models.BooleanField(default=False)),
                ('nombre_entidad', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tumores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tejido_mamario', models.BooleanField(default=False)),
                ('sistema_digestivo', models.BooleanField(default=False)),
                ('sistema_urinario', models.BooleanField(default=False)),
                ('otra_tumor', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValoracionesGerontologicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspecto_sociales', models.CharField(max_length=100)),
                ('aspecto_fisicos', models.CharField(max_length=100)),
                ('aspectos_funcional', models.CharField(max_length=100)),
                ('aspectos_psicogerontologico', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ValoracionesMentales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actual_pregunta', models.BooleanField(default=False)),
                ('dia_semana_pregunta', models.BooleanField(default=False)),
                ('lugar_pregunta', models.BooleanField(default=False)),
                ('lugar_nacimiento_pregunta', models.BooleanField(default=False)),
                ('presidente_pregunta', models.BooleanField(default=False)),
                ('primer_apellido_madre_pregunta', models.BooleanField(default=False)),
                ('resta_pregunta', models.BooleanField(default=False)),
                ('total_puntuacion_valoracion_mental', models.SmallIntegerField()),
                ('resultado', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='HistoriaGerontologica',
        ),
        migrations.AddField(
            model_name='aspectosfuncionales',
            name='fk_ayudas_ortopedicas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.ayudasortopedicas'),
        ),
        migrations.AddField(
            model_name='aspectospsicogerontologicos',
            name='fk_depresiones_yasavage',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.depresionesyasavage'),
        ),
        migrations.AddField(
            model_name='aspectospsicogerontologicos',
            name='fk_enfermedades_mentales',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.enfermedadesmentales'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_aspectos_funcionales',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.aspectosfuncionales'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_aspectos_psicogerontologicos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.aspectospsicogerontologicos'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_usuarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario'),
        ),
        migrations.AddField(
            model_name='evolucionesmensuales',
            name='fk_historias_gerontologicas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.historiasgerontologicas'),
        ),
        migrations.AddField(
            model_name='aspectosfuncionales',
            name='fk_indice_KATZ',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.indicekatz'),
        ),
        migrations.AddField(
            model_name='aspectosfisicos',
            name='fk_medicamentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medicamentos'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_relacion_familias',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.relacionfamilias'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_revision_sistemas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.revisionsistemas'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_cardiovasculares',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemascardiovasculares'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_digestivos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasdigestivos'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_endocrinos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasendocrinos'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_intergumentarios',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasintergumentarios'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_nerviosos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasnerviosos'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_oseo_musculares',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasoseosmusculares'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_respiratorios',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasrespiratorios'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_sistemas_urinarios',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.sistemasurinarios'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_situaciones_gerontologicas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.situacionesgerontologicas'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_tipo_familias',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipofamilias'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_tipo_protecciones_exequiales',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipoproteccionesexequiales'),
        ),
        migrations.AddField(
            model_name='revisionsistemas',
            name='fk_tumores',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.tumores'),
        ),
        migrations.AddField(
            model_name='historiasgerontologicas',
            name='fk_valoraciones_gerontologicas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.valoracionesgerontologicas'),
        ),
        migrations.AddField(
            model_name='aspectospsicogerontologicos',
            name='fk_valoraciones_mentales',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.valoracionesmentales'),
        ),
    ]
