# Generated by Django 2.2.4 on 2022-10-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20221013_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Cocina', 'Cocina'), ('Finanzas', 'Finanzas'), ('Garzón', 'Garzón'), ('Bodega', 'Bodega'), ('Administrador', 'Administrador')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
