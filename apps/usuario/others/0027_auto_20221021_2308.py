# Generated by Django 2.2.4 on 2022-10-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0026_auto_20221021_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Garzón', 'Garzón'), ('Bodega', 'Bodega'), ('Finanzas', 'Finanzas'), ('Cocina', 'Cocina'), ('Administrador', 'Administrador')], max_length=14, verbose_name='Rol'),
        ),
    ]
