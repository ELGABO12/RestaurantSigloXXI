# Generated by Django 2.2.4 on 2022-10-25 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_mesa', models.CharField(max_length=2, null=True, verbose_name='Número de la mesa')),
                ('descripcion_mesa', models.CharField(max_length=255, null=True, verbose_name='Descripción mesa')),
                ('cantidad_personas', models.CharField(max_length=2, null=True, verbose_name='Cantidad de personas')),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
                'ordering': ['numero_mesa'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=255, null=True, verbose_name='Nombre proveedor')),
                ('correo_proveedor', models.EmailField(max_length=255, null=True, verbose_name='Correo proveedor')),
                ('telefono_proveedor', models.CharField(max_length=12, null=True, verbose_name='Teléfono proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre_proveedor'],
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_receta', models.CharField(max_length=255, null=True, verbose_name='Nombre de la receta')),
                ('precio_receta', models.CharField(max_length=7, null=True, verbose_name='Precio de la receta')),
                ('tiempo_preparacion', models.CharField(max_length=2, null=True, verbose_name='Tiempo de preparación')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'ordering': ['nombre_receta'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('cantidad', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre_producto'],
            },
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(max_length=2, null=True, verbose_name='Cantidad')),
                ('productos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Producto')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Proveedor')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
                'ordering': ['proveedor'],
            },
        ),
    ]
