# Generated by Django 2.2.4 on 2022-10-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20221014_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Cocina', 'Cocina'), ('Garzón', 'Garzón'), ('Finanzas', 'Finanzas'), ('Bodega', 'Bodega')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
