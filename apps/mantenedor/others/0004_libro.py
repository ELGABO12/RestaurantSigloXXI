# Generated by Django 2.0.6 on 2022-08-29 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_remove_autor_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('autor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libro.Autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
