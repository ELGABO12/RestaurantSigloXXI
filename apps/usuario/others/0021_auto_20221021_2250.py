# Generated by Django 2.2.4 on 2022-10-22 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0020_auto_20221021_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Finanzas', 'Finanzas'), ('Cocina', 'Cocina'), ('Administrador', 'Administrador'), ('Bodega', 'Bodega'), ('Garzón', 'Garzón')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]