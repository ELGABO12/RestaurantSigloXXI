# Generated by Django 2.2.4 on 2022-10-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20221013_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Garzón', 'Garzón'), ('Administrador', 'Administrador'), ('Finanzas', 'Finanzas'), ('Cocina', 'Cocina'), ('Bodega', 'Bodega')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]