# Generated by Django 5.1.3 on 2024-11-27 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id_estudiante', models.IntegerField(unique=True)),
                ('_nombre', models.CharField(max_length=50)),
                ('_apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudiantePrimaria',
            fields=[
                ('gestor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gestor.gestor')),
                ('_grado', models.IntegerField()),
            ],
            bases=('Gestor.gestor',),
        ),
        migrations.CreateModel(
            name='EstudianteSecundaria',
            fields=[
                ('gestor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gestor.gestor')),
                ('_especialidad', models.CharField(max_length=50)),
            ],
            bases=('Gestor.gestor',),
        ),
    ]
