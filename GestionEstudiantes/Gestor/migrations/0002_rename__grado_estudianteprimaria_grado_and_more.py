# Generated by Django 5.1.3 on 2024-12-02 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudianteprimaria',
            old_name='_grado',
            new_name='grado',
        ),
        migrations.RenameField(
            model_name='estudiantesecundaria',
            old_name='_especialidad',
            new_name='especialidad',
        ),
        migrations.RenameField(
            model_name='gestor',
            old_name='_apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='gestor',
            old_name='_id_estudiante',
            new_name='id_estudiante',
        ),
        migrations.RenameField(
            model_name='gestor',
            old_name='_nombre',
            new_name='nombre',
        ),
    ]
