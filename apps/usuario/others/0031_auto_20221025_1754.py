# Generated by Django 2.2.4 on 2022-10-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0030_auto_20221024_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Cocina', 'Cocina'), ('Bodega', 'Bodega'), ('Administrador', 'Administrador'), ('Garzón', 'Garzón'), ('Finanzas', 'Finanzas')], max_length=14, verbose_name='Rol'),
        ),
    ]
