# Generated by Django 2.2.4 on 2022-10-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0023_auto_20221021_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Finanzas', 'Finanzas'), ('Administrador', 'Administrador'), ('Bodega', 'Bodega'), ('Cocina', 'Cocina'), ('Garzón', 'Garzón')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
