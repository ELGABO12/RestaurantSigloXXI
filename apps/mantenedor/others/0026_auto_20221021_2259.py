# Generated by Django 2.2.4 on 2022-10-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0025_auto_20221021_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='tiempo_preparacion',
            field=models.CharField(max_length=2, null=True, verbose_name='Tiempo de preparación'),
        ),
    ]
