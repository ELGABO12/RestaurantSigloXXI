# Generated by Django 2.2.4 on 2022-10-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_auto_20221019_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Finanzas', 'Finanzas'), ('Bodega', 'Bodega'), ('Garzón', 'Garzón'), ('Cocina', 'Cocina')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
