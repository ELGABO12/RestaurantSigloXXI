# Generated by Django 2.2.4 on 2022-11-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0008_auto_20221115_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='image',
            field=models.ImageField(blank=True, upload_to='apps/mantenedor//recetas'),
        ),
    ]
