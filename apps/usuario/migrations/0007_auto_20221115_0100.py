# Generated by Django 2.2.4 on 2022-11-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_auto_20221115_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Garzón', 'Garzón'), ('Cocina', 'Cocina'), ('Finanzas', 'Finanzas'), ('Bodega', 'Bodega')], max_length=14, verbose_name='Rol'),
        ),
    ]
