# Generated by Django 5.1.6 on 2025-03-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_contrasena_tlogin_contrasenalogin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tusuario',
            name='rol',
        ),
        migrations.AddField(
            model_name='tusuario',
            name='profesional',
            field=models.CharField(default='', max_length=255),
        ),
    ]
