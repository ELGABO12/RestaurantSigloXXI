# Generated by Django 2.0.6 on 2022-08-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_auto_20220828_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
