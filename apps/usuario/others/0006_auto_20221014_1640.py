# Generated by Django 2.2.4 on 2022-10-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20221013_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(blank=True, choices=[('Finanzas', 'Finanzas'), ('Bodega', 'Bodega'), ('Garzón', 'Garzón'), ('Administrador', 'Administrador'), ('Cocina', 'Cocina')], max_length=14, null=True, verbose_name='Rol'),
        ),
    ]
