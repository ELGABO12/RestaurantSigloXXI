# Generated by Django 2.2.4 on 2022-10-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_auto_20221019_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Garzón', 'Garzón'), ('Cocina', 'Cocina'), ('Bodega', 'Bodega'), ('Finanzas', 'Finanzas'), ('Administrador', 'Administrador')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
